**Introduction**\
This is a quick project to play around with python and snap. Tested on Ubuntu 16.04, sorry for missing pre-requisites!\
\
In mqtt/ping.py a MQTT client is initialized and connected to a broker.\
The client proceeds to poll the broker periodically.\
\
**Running with python**
```
git clone git@github.com:Laged/test-python-ping-mqtt.git
cd test-python-ping-mqtt
virtualenv -p /usr/bin/python2.7 test-env
source test-env/bin/activate
pip install -r requirements.txt
python main.py
...check output and http://www.hivemq.com/demos/websocket-client/? for ping attempts...
deactivate
```
\
**Running as a snap**
```
snapcraft
sudo snap try --devmode prime
sudo snap logs test-python-ping-mqtt -f
...check logs and http://www.hivemq.com/demos/websocket-client/? for ping attempts...
sudo snap remove test-python-ping-mqtt
```
\
**TODO**\
Figure out how to cross-compile this snap to armhf architecture.\
It SHOULD work with:
```
snapcraft --target-arch=armhf
```
But it raises an error:
```
NotImplementedError: The plugin used by 'test-python-ping-mqtt' does not support cross-compiling to a different target architecture
```
It seems like cross-compile support for the python plugin of snapcraft has not been implemented yet:\
https://forum.snapcraft.io/t/cross-compile-support-for-python-plugin/1286/3
