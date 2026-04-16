#include <Arduino.h>
#include <WiFi.h>
#include <esp_now.h>

struct CommandPayload {
    int vx;
    int vy;
    int dtheta;
} __attribute__((packed));

struct HeartbeatPayload {
    uint8_t robot_id;
} __attribute__((packed));

uint8_t broadcastAddress[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

#define SERIAL_CMD_HEADER_1 0xAA
#define SERIAL_CMD_HEADER_2 0xBB
#define SERIAL_HB_HEADER_1 0xCC
#define SERIAL_HB_HEADER_2 0xDD

enum SerialReadState {
    WAIT_HEADER_1,
    WAIT_HEADER_2,
    WAIT_LEN,
    WAIT_DATA
};
SerialReadState serialState = WAIT_HEADER_1;
uint8_t payloadLen;
uint8_t serialBuffer[250];
int serialBufferIdx = 0;

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
    if(len == sizeof(HeartbeatPayload)){
        Serial.write(SERIAL_HB_HEADER_1);
        Serial.write(SERIAL_HB_HEADER_2);
        Serial.write((uint8_t)len);
        Serial.write(incomingData, len);
    }
}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
}

void checkSerial() {
    while (Serial.available() > 0) {
        uint8_t b = Serial.read();
        switch (serialState) {
            case WAIT_HEADER_1:
                if (b == SERIAL_CMD_HEADER_1) {
                    serialState = WAIT_HEADER_2;
                }
                break;

            case WAIT_HEADER_2:
                if (b == SERIAL_CMD_HEADER_2) {
                    serialState = WAIT_LEN;
                } else {
                    serialState = WAIT_HEADER_1;
                }
                break;

            case WAIT_LEN:
                payloadLen = b;
                serialBufferIdx = 0;
                if (payloadLen > 0 && payloadLen <= 250) {
                    serialState = WAIT_DATA;
                } else {
                    serialState = WAIT_HEADER_1;
                }
                break;

            case WAIT_DATA:
                serialBuffer[serialBufferIdx++] = b;
                if (serialBufferIdx == payloadLen) {
                    esp_now_send(broadcastAddress, serialBuffer, payloadLen);
                    serialState = WAIT_HEADER_1;
                }
                break;
        }
    }
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    Serial.println("ESP-NOW Bridge");
    Serial.print("MAC Address: ");
    Serial.println(WiFi.macAddress());
    Serial.println("--------------------");
    if (esp_now_init() != ESP_OK) {
        Serial.println("Error initializing ESP-NOW");
        return;
    }
    esp_now_register_send_cb(OnDataSent);
    esp_now_register_recv_cb(OnDataRecv);
    esp_now_peer_info_t peerInfo;
    memset(&peerInfo, 0, sizeof(peerInfo));
    memcpy(peerInfo.peer_addr, broadcastAddress, 6);
    peerInfo.channel = 0;  
    peerInfo.ifidx = WIFI_IF_STA;
    peerInfo.encrypt = false;
    if (esp_now_add_peer(&peerInfo) != ESP_OK){
        Serial.println("Failed to add broadcast peer");
        return;
    }
    Serial.println("Bridge setup complete. Listening for Serial and ESP-NOW...");
}

void loop() {
    checkSerial();
}