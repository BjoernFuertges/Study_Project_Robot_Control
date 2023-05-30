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
To start the Gui navigate to `/webserver` then type:
```bash
python -m flask --app GUI run
```
to serve it in your browser

### GRPC start
Start the server:
```bash
python .\webcontroller\webcontroller.py
```

Start the client:
```bash
python .\webcontroller\webcontroller_client.py
```

## Rebuild
### proto
From `/webcontroller`
````bash
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/webcontroller.proto
```

# TODO Website:
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

# TODO Machine Learning/ Image Recognition:
1. start.