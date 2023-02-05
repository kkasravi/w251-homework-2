import logging
import boto3
from botocore.exceptions import ClientError
import os
import sys
import paho.mqtt.client as mqtt
import tempfile

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="kkasravi/face"
BUCKET_NAME=os.getenv("BUCKET_NAME")
OBJECT_NAME=os.getenv("OBJECT_NAME")

def upload_file(file_name, bucket, object_name):
    try:
        print(f"trying to upload file {file_name} to {bucket}")
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(f"caught exception {e}")
        return False
    return True

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
    try:
        data = msg.payload
        with open(tmp.name, 'w') as f:
            f.write(data)
        upload_file(tmp.name, BUCKET_NAME, OBJECT_NAME)
    except:
        print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message
s3_client = boto3.client('s3')
tmp = tempfile.NamedTemporaryFile()

# go into a loop
local_mqttclient.loop_forever()
