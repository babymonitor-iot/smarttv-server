import paho.mqtt.client as mqtt
import json
import time


# mosquitto_pub -h dojot.atlantico.com.br -p 1883  -t /gesad/9e4ed4/attrs -m '{"breathing": true, "crying": true, "from": "bm", "sleeping": true, "time_no_breathing": 0, "to": "smp", "type": "notification" }'


class ClientTV(mqtt.Client):
    def __init__(self):
        super().__init__("tv")
        self.on_connect = self.on_connect
        self.on_publish = self.on_publish
        self.connected = False

    # pub to bm in dojot
    def publish_to_dojot(self, data):
        self.connect(host="dojot.atlantico.com.br", port=1883)
        self.publish("/gesad/f0bf6d/attrs", payload=json.dumps(data), qos=1)
        self.disconnect()

    def on_publish(self, client, userdata, result):
        print('Message published')

    def on_connect(self, client, userdata, flags, rc):
        self.connected = True
        print("Connected with result code " + str(rc))

