# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2


# the index depends on your camera setup and which one is your USB camera.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
      # your logic goes here; for instance
      # cut out face from the frame.. 
      cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
      rc,png = cv2.imencode('.png', gray)
      # msg = png.tobytes()
      # ...

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
