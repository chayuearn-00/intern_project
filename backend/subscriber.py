import paho.mqtt.client as mqtt
import json
import os
from dotenv import load_dotenv
from influxdb import InfluxDBClient

# =========================
# Load ENV
# =========================
load_dotenv()

# MQTT Config
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC_ALL = "device"

# InfluxDB Config (v1)
INFLUX_HOST = os.getenv("INFLUX_HOST", "localhost")
INFLUX_PORT = int(os.getenv("INFLUX_PORT", "8086"))
INFLUX_USER = os.getenv("INFLUX_USER", "")
INFLUX_PASS = os.getenv("INFLUX_PASS", "")
INFLUX_DB = os.getenv("INFLUX_DB", "telegraf")

# =========================
# Connect InfluxDB
# =========================
influx_client = InfluxDBClient(
    host=INFLUX_HOST,
    port=INFLUX_PORT,
    username=INFLUX_USER,
    password=INFLUX_PASS,
    database=INFLUX_DB
)

print("✅ Connected to InfluxDB")

# =========================
# MQTT Callbacks
# =========================
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Connected to MQTT Broker at {MQTT_BROKER}")
        client.subscribe(TOPIC_ALL)
    else:
        print("❌ MQTT Connection Failed")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📩 Received from {msg.topic}: {payload}")

        json_body = [
            {
                "measurement": "MFEC",
                "tags": {
                    "device": "Device1" 
                },
                "fields": {
                    "battery": float(payload["battery"]),
                    "motor": float(payload["motor"]),
                    "sonar": float(payload["sonar"]),
                    "signal": float(payload["signal"])
                }
            }
        ]

        influx_client.write_points(json_body)
        print("📥 Data written to InfluxDB")

    except Exception as e:
        print("❌ Error processing message:", e)

# =========================
# Start MQTT Client
# =========================
client = mqtt.Client(client_id="Subscriber1")
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
