#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>

// === Comms ===

#define ROBOT_ID 1
#define RECV_START_PORT 8000
#define SEND_START_PORT 9000
#define SSID (char*)("Totalplay-D0AB")
#define PASSWORD (char*)("D0AB459EZxSqXN42")
#define TARGET_IP (char*)("192.168.100.196")
#define HEARTBEAT_INVERVAL 500

struct CommandPayload {
    int vx;
    int vy;
    int dtheta;
} __attribute__((packed));

struct HeartbeatPayload {
    uint8_t robot_id;
} __attribute__((packed));

WiFiUDP udp;
unsigned long prev_time = 0;

// === Motors pins ===

#define M1_PWM 4
#define M1_A 5
#define M1_B 6

#define M2_PWM 3
#define M2_A 7
#define M2_B 8

#define M3_PWM 1
#define M3_A 21
#define M3_B 20

#define M4_PWM 2
#define M4_A 10
#define M4_B 9

// === Movement settings ===

#define MIN_PWM 80
#define MAX_PWM 255
#define CORRECTION_FACTOR 4

// === Functions ===

void setMotor(int id, int pwm){
    pwm = constrain(pwm, -MAX_PWM, MAX_PWM);
    switch(id){
        case 0:
            digitalWrite(M1_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M1_B, pwm >= 0 ? LOW : HIGH);
            analogWrite(M1_PWM, abs(pwm));
            break;
        case 1:
            digitalWrite(M2_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M2_B, pwm >= 0 ? LOW : HIGH);
            analogWrite(M2_PWM, abs(pwm));
            break;
        case 2:
            digitalWrite(M3_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M3_B, pwm >= 0 ? LOW : HIGH);
            analogWrite(M3_PWM, abs(pwm));
            break;
        case 3:
            digitalWrite(M4_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M4_B, pwm >= 0 ? LOW : HIGH);
            analogWrite(M4_PWM, abs(pwm));
            break;
    }
}

void move(int vx, int vy, int dtheta) {
    float turn_correction = ((float)dtheta / 2.0f) * CORRECTION_FACTOR, pwm_f[4], max_pwm = 0;
    pwm_f[0] = (float)vy - (float)vx + turn_correction;
    pwm_f[1] = -(float)vy - (float)vx + turn_correction;
    pwm_f[2] = (float)vx - (float)vy + turn_correction;
    pwm_f[3] = (float)vy + (float)vx + turn_correction;
    for(int i = 0; i < 4; i++){
        if(abs(pwm_f[i]) > max_pwm){
            max_pwm = abs(pwm_f[i]);
        }
    }
    if(max_pwm > MAX_PWM){
        float scale = (float)MAX_PWM / max_pwm;
        for(int i = 0; i < 4; i++){
            pwm_f[i] *= scale;
        }
    }
    int pwm[4];
    for(int i = 0; i < 4; i++){
        if(abs(pwm_f[i]) < 1.0){
            pwm[i] = 0;
        }
        else{
            int sign = (pwm_f[i] > 0) ? 1 : -1;
            pwm[i] = sign * map(abs((long)pwm_f[i]), 1, MAX_PWM, MIN_PWM, MAX_PWM);
        }
    }
    for (int i = 0; i < 4; i++) {
        setMotor(i, pwm[i]);
    }
}

void recvPacket() {
    int packet_size = udp.parsePacket();
    if(packet_size == sizeof(CommandPayload)){
        CommandPayload cmd;
        udp.read((uint8_t*)&cmd, sizeof(CommandPayload));
        Serial.printf("Received Command: vx=%d, vy=%d, dtheta=%d\n", cmd.vx, cmd.vy, cmd.dtheta);
        move(cmd.vx, cmd.vy, cmd.dtheta);
    }
}

void sendPacket() {
    if(millis() - prev_time > HEARTBEAT_INVERVAL){
        prev_time = millis();
        HeartbeatPayload hb;
        hb.robot_id = ROBOT_ID;
        udp.beginPacket(TARGET_IP, SEND_START_PORT + ROBOT_ID);
        udp.write((uint8_t*)&hb, sizeof(HeartbeatPayload));
        udp.endPacket();
        Serial.printf("Sent heartbeat to %s:%d\n", TARGET_IP, SEND_START_PORT + ROBOT_ID);
    }
}

void setPins(){
    pinMode(M1_PWM, OUTPUT);
    pinMode(M1_A, OUTPUT);
    pinMode(M1_B, OUTPUT);
    pinMode(M2_PWM, OUTPUT);
    pinMode(M2_A, OUTPUT);
    pinMode(M2_B, OUTPUT);
    pinMode(M3_PWM, OUTPUT);
    pinMode(M3_A, OUTPUT);
    pinMode(M3_B, OUTPUT);
    pinMode(M4_PWM, OUTPUT);
    pinMode(M4_A, OUTPUT);
    pinMode(M4_B, OUTPUT);
}

void setWiFi(){
    WiFi.begin(SSID, PASSWORD);
    while(WiFi.status() != WL_CONNECTED){
        delay(500);
        Serial.print(".");
    }
    Serial.println(" CONNECTED!");
    Serial.printf("IP Address: %s\n", WiFi.localIP());
    if(udp.begin(RECV_START_PORT + ROBOT_ID)){
        Serial.printf("UDP listener started on port %d\n", RECV_START_PORT + ROBOT_ID);
        //digitalWrite(8, HIGH);
    }
    else{
        Serial.println("Failed to start UDP listener.");
        while(true){
            digitalWrite(8, LOW);
            delay(500);
            digitalWrite(8, HIGH);
            delay(500);
        }
    }
}

// === Program ===

void setup(){
    setPins();
    /*
    Serial.begin(115200);
    pinMode(8, OUTPUT);
    digitalWrite(8, LOW);
    delay(100);
    Serial.println();
    Serial.printf("ESP32 Robot Controller - ID: %d\n", ROBOT_ID);
    Serial.printf("Connecting to %s ", SSID);
    setWiFi();
    */
}

void loop(){
    //recvPacket();
    //sendPacket();
    for(int i = 0; i < 4; i++){
        setMotor(i, 100);
    }
}