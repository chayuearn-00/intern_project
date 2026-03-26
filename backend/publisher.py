import paho.mqtt.client as mqtt
import json
import time
import random
import threading
import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Configuration
# ==========================================
BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC_ALL = "device"

# สร้าง MQTT Client
client = mqtt.Client(client_id="Publisher1")

# Callback เมื่อเชื่อมต่อสำเร็จ
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Connected to MQTT Broker at {BROKER}")
    else:
        print(f"❌ Connection failed with code {rc}")

client.on_connect = on_connect



# ==========================================
# Task 1: Energy Publisher (ทำงานทุก 5 วินาที)
# ==========================================
def publish():
    while True:
        try:
            payload = {
                "battery": random.randint(0, 100),
                "motor": random.randint(0, 100),
                "signal": random.randint(0, 100),
                "sonar": random.randint(375, 400),
            }
            
            # for i in range(1, 6):
                # สร้าง ID ให้ตรงกับที่ Dashboard คาดหวัง (cu_energy001 - 005)
                # meter_id = f"cu_energy00{i}"
                
                # payload = {
                #     "motor": meter_id,  # ปรับ key ให้สื่อความหมายชัดเจน
                #     "": random.randint(375, 400), # จำลองไฟ 3 เฟส (380V range)
                #     "voltage_bc": random.randint(375, 400),
                #     "voltage_ca": random.randint(375, 400)
                # }
                
                # # Publish ข้อมูล
            client.publish(TOPIC_ALL, json.dumps(payload))
            print(f"{payload}")
                
            time.sleep(5) # รอ 5 วินาที
            
        except Exception as e:
            print(f"Error in Energy Thread: {e}")
            time.sleep(5)

# ==========================================
# Main Execution
# ==========================================
if __name__ == "__main__":
    try:
        # 1. เชื่อมต่อ MQTT
        # print("Connecting to MQTT Broker...")
        client.connect(BROKER, PORT, 60)
        
        # เริ่ม Loop การทำงานของ MQTT ใน Background (สำหรับรับ-ส่งข้อมูลพื้นฐาน)
        client.loop_start()

        # 2. สร้าง Thread แยกสำหรับการส่งข้อมูล 2 ประเภท
        # เพื่อให้ Time.sleep ของแต่ละอันไม่รอกัน (Non-blocking)
        thread_devices = threading.Thread(target=publish)
        # thread_sensor = threading.Thread(target=publish_sensors)

        # 3. เริ่มรัน Thread
        thread_devices.daemon = True # ตั้งเป็น Daemon เพื่อให้ปิดโปรแกรมแล้ว Thread ดับด้วย
        # thread_sensor.daemon = True
        
        thread_devices.start()
        # thread_sensor.start()

        # ปล่อยให้ Main Thread รอ (กด Ctrl+C เพื่อหยุด)
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping Publisher...")
        client.loop_stop()
        client.disconnect()
        print("Goodbye!")