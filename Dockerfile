FROM arm32v7/python:3.6-slim-bullseye

RUN apt-get update
RUN apt-get install -y gcc libgpiod2

RUN pip3 install --upgrade pip
RUN CFLAGS="-fcommon" pip3 install --upgrade rpi.gpio
RUN pip3 install adafruit-circuitpython-dht
RUN pip3 install paho-mqtt

WORKDIR /home
COPY src ./src

ENTRYPOINT ["python3", "src/dht22.py"]
