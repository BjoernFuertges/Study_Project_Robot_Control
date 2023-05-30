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
To start the Gui navigate to `/website` then type:
```bash
cd robotcontrol
python gui_handler.py
```
(real setup)
or
```bash
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
From `/robotcontroll`
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

### TODO Machine Learning/ Image Recognition:
1. start.