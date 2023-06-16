from queue import Queue
from threading import Thread
import robot_control_system.move as move
from robot_control_system.move import Move_Command

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

# A thread that produces data
def ui(out_q, robot_name : str, wc_ip : str, wc_port : int):
    while(True):
        with grpc.insecure_channel(wc_ip + ":" + str(wc_port)) as channel:
            stub = webcontroller_pb2_grpc.AgentStub(channel)
            response = stub.MoveInformationHasNew(webcontroller_pb2.MoveInformationRequest(name=robot_name))
            
            print(response.hasNew)

            if response.hasNew:
                response = stub.MoveInformation(webcontroller_pb2.MoveInformationRequest(name=robot_name))
                
                mc = Move_Command()
                mc.set_direction(response.direction)
                mc.set_radius(response.radius)
                mc.set_speed(response.speed)
                mc.set_stop_working(response.stop)
                mc.set_turn(response.turn)

                print(mc.to_string())

                out_q.put(mc)

                if mc.get_stop_working:
                    print("Stop!")
                    break
          
def start(name : str, wc_ip : str, wc_port : int) -> None:
    # Create the shared queue and launch both threads
    working_queue = Queue()
    t_mh = Thread(target = move.move_handler, args =(working_queue, ))
    t_ui = Thread(target = ui, args =(working_queue, name, wc_ip, wc_port,))
    t_mh.start()
    t_ui.start()
    
    # Wait for all produced items to be consumed
    working_queue.join()