#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>

// === Comms ===
#define ROBOT_ID 1
#define RECV_START_PORT 8000
#define SEND_START_PORT 9000
#define HEARTBEAT_INVERVAL 500
//const char* SSID = "Totalplay-D0AB";
//const char* PASSWORD = "D0AB459EZxSqXN42";
//const char* TARGET_IP = "192.168.100.196";
const char* SSID = "robot_1";
const char* PASSWORD = "robot123";
const char* TARGET_IP = "192.168.0.131";

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
#define M1_PWM 1
#define M1_A 20
#define M1_B 21

#define M2_PWM 2
#define M2_A 10
#define M2_B 9

#define M3_PWM 4
#define M3_A 5
#define M3_B 6

#define M4_PWM 3
#define M4_A 7
#define M4_B 8

constexpr int M1_CHANNEL = 0;
constexpr int M2_CHANNEL = 1;
constexpr int M3_CHANNEL = 2;
constexpr int M4_CHANNEL = 3;

// === Movement settings ===

constexpr int MIN_PWM = 80;
constexpr int MAX_PWM = 250;
constexpr int CORRECTION_FACTOR = 1;

// === Functions ===

void setMotors(int m1_speed, int m2_speed, int m3_speed, int m4_speed){
    uint32_t set_mask = 0;
    uint32_t clear_mask = 0;

    set_mask |= (m1_speed > 0) ? (1 << M1_A) : (1 << M1_B);
    clear_mask |= (m1_speed > 0) ? (1 << M1_B) : (1 << M1_A);
    ledcWrite(M1_CHANNEL, abs(m1_speed));

    set_mask |= (m2_speed > 0) ? (1 << M2_A) : (1 << M2_B);
    clear_mask |= (m2_speed > 0) ? (1 << M2_B) : (1 << M2_A);
    ledcWrite(M2_CHANNEL, abs(m2_speed));

    set_mask |= (m3_speed > 0) ? (1 << M3_A) : (1 << M3_B);
    clear_mask |= (m3_speed > 0) ? (1 << M3_B) : (1 << M3_A);
    ledcWrite(M3_CHANNEL, abs(m3_speed));
    
    set_mask |= (m4_speed > 0) ? (1 << M4_A) : (1 << M4_B);
    clear_mask |= (m4_speed > 0) ? (1 << M4_B) : (1 << M4_A);
    ledcWrite(M4_CHANNEL, abs(m4_speed));

    GPIO.out_w1ts.val = set_mask;
    GPIO.out_w1tc.val = clear_mask;
}

void move(int vx, int vy, int dtheta) {
    long turn_correction = dtheta * CORRECTION_FACTOR; 
    long vel[4];
    int pwm[4];
    long max_vel = 0;

    vel[0] = vy - vx + turn_correction;
    vel[1] = vy + vx + turn_correction;
    vel[2] = -vy + vx + turn_correction;
    vel[3] = -vy - vx + turn_correction;

    for(int i = 0; i < 4; i++){
        if(abs(vel[i]) > max_vel){
            max_vel = abs(vel[i]);
        }
    }

    if(max_vel > 0){
        for(int i = 0; i < 4; i++){
            if(max_vel > MAX_PWM){
                vel[i] = (vel[i] * MAX_PWM) / max_vel;
            }
            if(abs(vel[i]) < 10){
                pwm[i] = 0;
            }
            else{
                int sign = (vel[i] > 0) ? 1 : -1;
                pwm[i] = sign * (MIN_PWM + ((abs(vel[i]) - 1) * (MAX_PWM - MIN_PWM)) / (MAX_PWM - 1));
            }
        }
    }
    else{
        for(int i = 0; i < 4; i++){
            pwm[i] = 0;
        }
    }
    setMotors(pwm[0], pwm[1], pwm[2], pwm[3]);
}

void recvPacket() {
    if(udp.parsePacket() == sizeof(CommandPayload)){
        CommandPayload cmd;
        udp.read((uint8_t*)&cmd, sizeof(CommandPayload));
        move(cmd.vx, cmd.vy, cmd.dtheta);
    }
}

void sendPacket() {
    if(millis() - prev_time > HEARTBEAT_INVERVAL){
        HeartbeatPayload hb;
        hb.robot_id = ROBOT_ID;
        udp.beginPacket(TARGET_IP, SEND_START_PORT + ROBOT_ID);
        udp.write((uint8_t*)&hb, sizeof(HeartbeatPayload));
        udp.endPacket();
        prev_time = millis();
    }
}

void setPins(){
    pinMode(M1_A, OUTPUT);
    pinMode(M1_B, OUTPUT);
    pinMode(M2_A, OUTPUT);
    pinMode(M2_B, OUTPUT);
    pinMode(M3_A, OUTPUT);
    pinMode(M3_B, OUTPUT);
    pinMode(M4_A, OUTPUT);
    pinMode(M4_B, OUTPUT);
    
    ledcSetup(M1_CHANNEL, 5000, 8);
    ledcSetup(M2_CHANNEL, 5000, 8);
    ledcSetup(M3_CHANNEL, 5000, 8);
    ledcSetup(M4_CHANNEL, 5000, 8);

    ledcAttachPin(M1_PWM, M1_CHANNEL);
    ledcAttachPin(M2_PWM, M2_CHANNEL);
    ledcAttachPin(M3_PWM, M3_CHANNEL); 
    ledcAttachPin(M4_PWM, M4_CHANNEL);
}

void setWiFi(){
    WiFi.begin(SSID, PASSWORD);
    bool active = true;
    while(WiFi.status() != WL_CONNECTED){
        Serial.print(".");
        digitalWrite(8, active);
        active = !active;
        delay(500);
    }
    Serial.println(" CONNECTED!");
    Serial.printf("IP Address: %s\n", WiFi.localIP().toString().c_str());
    if(udp.begin(RECV_START_PORT + ROBOT_ID)){
        Serial.printf("UDP listener started on port %d\n", RECV_START_PORT + ROBOT_ID);
    }
    else{
        Serial.println("Failed to start UDP listener.");
        while(true){
            digitalWrite(8, LOW);
            delay(100);
            digitalWrite(8, HIGH);
            delay(100);
        }
    }
}

// === Program ===

void setup(){
    Serial.begin(115200);
    pinMode(8, OUTPUT);
    setWiFi();
    Serial.end(); 
    delay(500);
    setPins();
    setMotors(0, 0, 0, 0);
}

void loop(){
    recvPacket();
    sendPacket();
}

/*
#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>

// === Comms ===

#define ROBOT_ID 0
#define RECV_START_PORT 8000
#define SEND_START_PORT 9000
//#define SSID (char*)("Totalplay-D0AB")
//#define PASSWORD (char*)("D0AB459EZxSqXN42")
//#define TARGET_IP (char*)("192.168.100.196")
#define SSID (char*)("robot_1")
#define PASSWORD (char*)("robot123")
#define TARGET_IP (char*)("192.168.0.131")
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
bool online = false;

// === Motors pins ===

#define M1_PWM 1
#define M1_A 20
#define M1_B 21

#define M2_PWM 2
#define M2_A 10
#define M2_B 9

#define M3_PWM 4
#define M3_A 5
#define M3_B 6

#define M4_PWM 3
#define M4_A 7
#define M4_B 8


// === Movement settings ===

#define MIN_PWM 80
#define MAX_PWM 255
#define CORRECTION_FACTOR 1

// === Functions ===

void setMotor(int id, int pwm){
    pwm = constrain(pwm, -MAX_PWM, MAX_PWM);
    switch(id){
        case 0:
            digitalWrite(M1_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M1_B, pwm > 0 ? LOW : HIGH);
            analogWrite(M1_PWM, abs(pwm));
            break;
        case 1:
            digitalWrite(M2_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M2_B, pwm > 0 ? LOW : HIGH);
            analogWrite(M2_PWM, abs(pwm));
            break;
        case 2:
            digitalWrite(M3_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M3_B, pwm > 0 ? LOW : HIGH);
            analogWrite(M3_PWM, abs(pwm));
            break;
        case 3:
            digitalWrite(M4_A, pwm > 0 ? HIGH : LOW);
            digitalWrite(M4_B, pwm > 0 ? LOW : HIGH);
            analogWrite(M4_PWM, abs(pwm));
            break;
    }
}

void setMotors(int m1_speed, int m2_speed, int m3_speed, int m4_speed) {
    uint32_t set_mask = 0;
    uint32_t clear_mask = 0;
    if(m1_speed > 0) {
        set_mask |= (1 << M1_A);
        clear_mask |= (1 << M1_B);
    }
    else{
        clear_mask |= (1 << M1_A);
        set_mask |= (1 << M1_B);
    }
    ledcWrite(0, abs(m1_speed));

    if(m2_speed > 0){
        set_mask |= (1 << M2_A);
        clear_mask |= (1 << M2_B);
    }
    else{
        clear_mask |= (1 << M2_A);
        set_mask |= (1 << M2_B);
    }
    ledcWrite(1, abs(m2_speed));

    if(m3_speed > 0){
        set_mask |= (1 << M3_A);
        clear_mask |= (1 << M3_B);
    }
    else{
        clear_mask |= (1 << M3_A);
        set_mask |= (1 << M3_B);
    }
    ledcWrite(2, abs(m3_speed));
    
    if(m4_speed > 0){
        set_mask |= (1 << M4_A);
        clear_mask |= (1 << M4_B);
    } else {
        clear_mask |= (1 << M4_A);
        set_mask |= (1 << M4_B);
    }
    ledcWrite(3, abs(m4_speed));

    GPIO.out_w1ts.val = set_mask;
    GPIO.out_w1tc.val = clear_mask;
}

void move(int vx, int vy, int dtheta) {
    int turn_correction = (float)dtheta * (float)CORRECTION_FACTOR, 
        vel[4], 
        pwm[4],
        max_pwm = 0;
    vel[0] = vy - vx + turn_correction;
    vel[1] = vy + vx + turn_correction;
    vel[2] = -vy + vx + turn_correction;
    vel[3] = -vy - vx + turn_correction;
    for(int i = 0; i < 4; i++){
        if(abs(vel[i]) > max_pwm){
            max_pwm = abs(vel[i]);
        }
    }
    float scale = (float)MAX_PWM / (float)max_pwm;
    for(int i = 0; i < 4; i++){
        if(max_pwm > MAX_PWM){
            vel[i] = (float)vel[i] * scale;
        }
        if(abs(vel[i]) < 10){
            pwm[i] = 0;
        }
        else{
            int sign = (vel[i] > 0) ? 1 : -1;
            pwm[i] = sign * map(abs(vel[i]), 1, 255, MIN_PWM, MAX_PWM);
        }
        //setMotor(i, pwm[i]);
    }
    setMotors(pwm[0], pwm[1], pwm[2], pwm[3]);
}

void recvPacket() {
    int packet_size = udp.parsePacket();
    if(packet_size == sizeof(CommandPayload)){
        CommandPayload cmd;
        udp.read((uint8_t*)&cmd, sizeof(CommandPayload));
        //Serial.printf("Received Command: vx=%d, vy=%d, dtheta=%d\n", cmd.vx, cmd.vy, cmd.dtheta);
        move(cmd.vx, cmd.vy, cmd.dtheta);
    }
}

void sendPacket() {
    if(millis() - prev_time > HEARTBEAT_INVERVAL){
        HeartbeatPayload hb;
        hb.robot_id = ROBOT_ID;
        udp.beginPacket(TARGET_IP, SEND_START_PORT + ROBOT_ID);
        udp.write((uint8_t*)&hb, sizeof(HeartbeatPayload));
        udp.endPacket();
        prev_time = millis();
    }
}

void setPins(){
    pinMode(M1_PWM, OUTPUT);
    pinMode(M1_A, OUTPUT);
    pinMode(M1_B, OUTPUT);
    pinMode(M2_A, OUTPUT);
    pinMode(M2_B, OUTPUT);
    pinMode(M3_A, OUTPUT);
    pinMode(M3_B, OUTPUT);
    pinMode(M4_A, OUTPUT);
    pinMode(M4_B, OUTPUT);

    ledcSetup(0, 5000, 8);
    ledcSetup(1, 5000, 8);
    ledcSetup(2, 5000, 8);
    ledcSetup(3, 5000, 8);
    ledcAttachPin(M1_PWM, 0);
    ledcAttachPin(M2_PWM, 1);
    ledcAttachPin(M3_PWM, 2);
    ledcAttachPin(M4_PWM, 3);
}

void setWiFi(){
    WiFi.begin(SSID, PASSWORD);
    bool active = false;
    while(WiFi.status() != WL_CONNECTED){
        Serial.print(".");
        digitalWrite(8, active ? HIGH : LOW);
        active != active;
        delay(500);
    }
    Serial.println(" CONNECTED!");
    Serial.printf("IP Address: ");
    Serial.println(WiFi.localIP());
    if(udp.begin(RECV_START_PORT + ROBOT_ID)){
        Serial.printf("UDP listener started on port %d\n", RECV_START_PORT + ROBOT_ID);
        online = true;
    }
    else{
        Serial.println("Failed to start UDP listener.");
        online = false;
    }
}

// === Program ===

void setup(){
    Serial.begin(115200);
    pinMode(8, OUTPUT);
    setWiFi();
    Serial.end();
    delay(500);
    setPins();

    setMotors(0, 0, 0, 0);
     
    while(!online){
        digitalWrite(8, LOW);
        delay(100);
        digitalWrite(8, HIGH);
        delay(100);
    }
    
}

void loop(){
    recvPacket();
    sendPacket();
}
*/