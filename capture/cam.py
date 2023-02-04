# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import paho.mqtt.client as mqtt
import cv2

LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=30926
LOCAL_MQTT_TOPIC="kkasravi/face"

# the index depends on your camera setup and which one is your USB camera.
face_cascade_name = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_name)
cap = cv2.VideoCapture(0)

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    #-- Detect faces
    try:
        faces = face_cascade.detectMultiScale(frame_gray)
        for (x,y,w,h) in faces:
            center = (x + w//2, y + h//2)
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
    except:
        print("caught exception")
    # cv2.imshow('Capture - Face detection', frame)
    img_encode = cv2.imencode('.png', frame)[1]
    data_encode = np.array(img_encode)
    msg = data_encode.tobytes()
    local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if frame is not None:

        detectAndDisplay(frame)

    if cv2.waitKey(10) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
