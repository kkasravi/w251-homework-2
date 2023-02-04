FROM ubuntu
  
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /app
RUN apt-get update
#RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev
RUN apt install -y python3-dev python3-pip  vim-tiny libgl1-mesa-glx libglib2.0-0 libx11-xcb1
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt
RUN pip3 install opencv-python==3.4.18.65 opencv-contrib-python==3.4.18.65
# example from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
COPY cam.py cam.py
#COPY haarcascade-frontalface_alt.xml haarcascade-frontalface_alt.xml
COPY haarcascade-frontalface_default.xml haarcascade-frontalface_default.xml

CMD ["python3","cam.py"]
