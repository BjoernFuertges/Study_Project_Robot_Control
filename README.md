# Studienprojekt1_Robotersteuerung

## Dependencies
### Webserver
* Flask:
    ```bash
    pip install flask
    ```

### webcontroller
* grpc
    ```bash
    pip install grpcio-tools
    ```
## Start
To start the Gui navigate to `/robotcontrol` then type:
```bash
python gui_handler.py
```
(real setup)
or
```bash
cd website
python -m flask --app GUI run
```
(dry run)
to serve it in your browser

### GRPC start
Start the server:
```bash
cd robotcontrol
python server_handler.py
```

Start the client:
```bash
cd robotcontrol
python gui_handler.py
```

## Rebuild
### proto
From `/robotcontrol`
```bash
python -m grpc_tools.protoc -I./protos --python_out=./protos_generated --pyi_out=./protos_generated --grpc_python_out=./protos_generated ./protos/webcontroller.proto
```
**Insert per hand `protos_generated.` in webcontroller_pb2_grpc.py in the import line (`import webcontroller_pb2 as webcontroller__pb2`)!** If you don't do it, the programm will not run because of an `ModuleNotFoundError`.

## TODO
### TODO Website:
0. Complete interface for Robot Controls
    0.1 Make a connection to the Camera and show the camera output on the webserver
    0.2 Show how much the wheels are turned in real time
1. Arrow Key Controls with W A S D
2. Do some more styling
    1. on hover effects
    2. new header
    3. Logo for RCI
3. Fill about site
4. Fill Data site
5. Display response from the webcontroller-server on the website.
6. Replace the previous point with: Display the actual status of the robot (fetch periodically).
# Adeept 4WD Smart Car Kit for Raspberry Pi PiCar-B

## About This Product

## About Adeept

Adeept is a technical service team of open source software and hardware. Dedicated to applying the Internet and the latest industrial technology in open source area, we strive to provide best hardware support and software service for general makers and electronic enthusiasts around the world. We aim to create infinite possibilities with sharing. No matter what field you are in, we can lead you into the electronic world and bring your ideas into reality.

## Contact Info
 Technical Support:  support@adeept.com<br/>
 Customer Service:   service@adeept.com<br/>
 Website:            www.adeept.com<br/>


## Dependencies
```
pip install RPi.GPIO  
pip install rpi-ws281x
pip install Adafruit-PCA9685
```

**You have to activate the i2c interface**

## Deleted files
* LED.py: no LED strip available
* LEDapp.py: no LED strip available
* findline.py: unnecessary
* FPV.py: unnecessary
* FPVtest.py: unnecessary
* camera_opencv.py: unnecessary
* app.py: unnecessary
* appserver.py: unnecessary
* appserverAP.py: unnecessary
* webServer.py: unnecessary
* SR.py: unnecessary
* server.py: unnecessary
* serverTest.py: unnecessary
* OLED.py: unnecessary
* robotLight.py: unnecessary
* GUIfindline.py: unnecessary
* GUImove.py: unnecessary
* switch.py: unnecessary
* setup.py: redundant
* Instruction.txt: unnecessary (no information provided)

## Questions
* Are RPIservo and servo redundant?
### TODO Machine Learning/ Image Recognition:
1. start.