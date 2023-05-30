from queue import Queue
from threading import Thread
import move
from move import Move_Command

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

robot_name = "IRobot"

# A thread that produces data
def ui(out_q):
    while(True):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = webcontroller_pb2_grpc.AgentStub(channel)
            response = stub.MoveInformationHasNew(webcontroller_pb2.MoveInformationRequest(name=robot_name))
            
            if response.hasNew:
                response = stub.MoveInformation(webcontroller_pb2.MoveInformationRequest(name=robot_name))
                
                mc = Move_Command()
                mc.set_direction(response.direction)
                mc.set_radius(response.radius)
                mc.set_speed(response.speed)
                mc.set_stop_working(response.stop)
                mc.set_turn(response.turn)

                out_q.put(mc)

                if mc.get_stop_working:
                    break
          
# Create the shared queue and launch both threads
working_queue = Queue()
t_mh = Thread(target = move.move_handler, args =(working_queue, ))
t_ui = Thread(target = ui, args =(working_queue, ))
t_mh.start()
t_ui.start()
  
# Wait for all produced items to be consumed
working_queue.join()