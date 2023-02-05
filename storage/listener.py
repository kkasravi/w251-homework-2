import boto3
from botocore.exceptions import ClientError
import os
import paho.mqtt.client as mqtt
import tempfile

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="kkasravi/face"
BUCKET_NAME=os.getenv("BUCKET_NAME")
OBJECT_NAME=os.getenv("OBJECT_NAME")
ACCESS_KEY=os.getenv("ACCESS_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")

def upload_file(file_name, bucket, object_name):
    try:
        print(f"trying to upload file {file_name} to {bucket}")
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(f"caught exception {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    return True

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client, userdata, msg):
    try:
        print("in on_message")
        data = msg.payload
        with open(tmpfile.name, 'w') as f:
            f.write(str(data))
        upload_file(tmpfile.name, BUCKET_NAME, OBJECT_NAME)
    except Exception as e:
        print(f"Unexpected error: {e}")

s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
tmpfile = tempfile.NamedTemporaryFile()

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
print("before loop_forever")
local_mqttclient.loop_forever()
