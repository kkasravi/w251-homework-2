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

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
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
s3 = boto3.client('s3')
tmp = tempfile.NamedTemporaryFile()

# go into a loop
local_mqttclient.loop_forever()
