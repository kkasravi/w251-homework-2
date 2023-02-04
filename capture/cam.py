# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import paho.mqtt.client as mqtt
import cv2

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="kkasravi/face"

# the index depends on your camera setup and which one is your USB camera.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rc, png = cv2.imencode('.png', gray)
    msg = png.tobytes()

    local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)

#    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#    for (x,y,w,h) in faces:
#      cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
#      rc,png = cv2.imencode('.png', gray)
      # msg = png.tobytes()
      # ...

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
