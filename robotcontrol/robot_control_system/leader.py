import os
import time
from queue import Queue
from threading import Thread
import robot_control_system.move as move
from robot_control_system.move_command import Move_Command

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

# A thread that produces data
def ui(out_q, robot_name : str, wc_ip : str, wc_port : int, stop):
    while(stop() != True):
        with grpc.insecure_channel(wc_ip + ":" + str(wc_port)) as channel:
            stub = webcontroller_pb2_grpc.AgentStub(channel)
            response = stub.MoveInformationHasNew(webcontroller_pb2.MoveInformationRequest(name=robot_name))
            

            if response.hasNew == True:
                print(response.hasNew)
                
                response = stub.MoveInformationGetNew(webcontroller_pb2.MoveInformationRequest(name=robot_name))
                
                mc = Move_Command()
                mc.set_direction(response.direction)
                mc.set_radius(response.radius)
                mc.set_speed(response.speed)
                mc.set_stop_working(response.stop)
                mc.set_turn(response.turn)

                print(mc.to_string())

                out_q.put(mc)

                if mc.get_stop_working():
                    print("Stop!")
                    continue

def image_handler(image_intervall : int, image_folder : str, chunk_size : int, stop) -> None:
    while(stop() != True):
        files = os.listdir(image_folder)
        for file in files:
            with open(file, "rb") as image_file:
                image_value = image_file.read()
                byte_arr = bytearray(image_value)

            with grpc.insecure_channel(wc_ip + ":" + str(wc_port)) as channel:
                stub = webcontroller_pb2_grpc.AgentStub(channel)
                
                while len(byte_arr) > 0:
                    if len(byte_arr) < chunk_size:
                        chunk = byte_arr
                        byte_arr = []
                    else:
                        chunk = byte_arr[0 : chunk_size]
                        byte_arr = byte_arr[chunk_size : ]
                    response = stub.ImageReceiverChunker(chunk)

            os.remove(file)

        times.sleep(image_intervall)

         
def start(name : str, wc_ip : str, wc_port : int, picture_intervall : int, tmp_img_folder : str, chunk_size : int) -> None:
    
    # Create the shared queue and launch both threads
    working_queue = Queue()
    m = move.Move(tmp_img_folder=tmp_img_folder)
    stop_threads = False
    t_ih = Thread(target = image_handler, args =(picture_intervall, tmp_img_folder, chunk_size, lambda: stop_threads))
    t_mh = Thread(target = m.move_handler, args =(working_queue, lambda: stop_threads, picture_intervall))
    t_ui = Thread(target = ui, args =(working_queue, name, wc_ip, wc_port, lambda: stop_threads))

    t_ih.start()
    t_mh.start()
    t_ui.start()

    try:
        # Wait for all produced items to be consumed
        working_queue.join()
    except KeyboardInterrupt:
        stop_threads = True
        t_mh.join()
        t_ui.join()
        print("Bye")