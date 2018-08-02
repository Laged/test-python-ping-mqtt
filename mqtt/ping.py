import socket
from time import sleep

import paho.mqtt.client as mqtt

hostname      = socket.gethostname()
broker        = 'broker.hivemq.com'
port          = 1883
default_user  = hostname
default_pw    = None
default_topic = '/ping-mqtt/' + hostname
default_msg   = 'ping'
default_qos   = 0
ping_interval = 1
running       = True
subscribed    = False

def __ping_loop(client):
    while running:
      if subscribed:
          print 'Pinging',default_topic
          client.publish(default_topic, default_msg)
      sleep(ping_interval)

def __on_connect(client, userdata, flags, rc):
    if rc == 0:
        username = userdata['user'] if 'user' in userdata else None
        print 'Connection',str(username),'to',str(client._host)+':'+str(client._port),'OK'
        print 'Subscribing to',str(default_topic),'with QoS',str(default_qos)
        client.subscribe(default_topic, default_qos)
    else:
        print 'Connection failed with code',rc

def __on_message(client, userdata, msg):
    print 'Message ' + msg.topic+': '+str(msg.payload)

def __on_subscribe(client, userdata, mid, granted_qos):
    topic =  userdata['topic'] if 'topic' in userdata else None
    print 'Subscription to',topic,'with QoS',str(granted_qos),'OK'
    global subscribed
    subscribed = True

def init():
    print 'Initializing client that pings a MQTT broker'
    defaults = {
        'user':default_user,
        'password':default_pw,
        'topic': default_topic,
        'msg': default_msg
    }
    client = mqtt.Client()
    client.username_pw_set(default_user, default_pw)
    client.user_data_set(defaults)
    client.on_connect = __on_connect
    client.on_message = __on_message
    client.on_subscribe = __on_subscribe

    print 'Connecting',hostname,'to',broker+':'+str(port)
    client.loop_start()
    client.connect(broker, port)
    __ping_loop(client)

if __name__ == '__main__':
    init()
