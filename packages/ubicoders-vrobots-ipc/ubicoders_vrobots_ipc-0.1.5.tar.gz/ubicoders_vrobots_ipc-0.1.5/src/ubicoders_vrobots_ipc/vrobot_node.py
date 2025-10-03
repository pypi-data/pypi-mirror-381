from typing import Callable, Dict, Tuple, Optional, Any, List
from ubicoders_vrobots_msgs.states_msg_helper import VRobotState, StatesMsg, StatesMsgT
from .node_iox2 import ImageResolution, Iox2Node
from .node_zenoh import ZenohNode
from .node_iox2_utils import *
import time
from colorama import Fore, Style, Back

def vrobot_client_runner(vrobot_nodes: List[Any]):
    vrclient = VRobotClient()
    for node in vrobot_nodes:
        vrclient.add_vrobot_node(node)
    try:
        while True:
            vrclient.update()            
            time.sleep(0.02) # sim does not update faster than 50Hz at the best case.
    finally:
        print(f"Shutting down...")
        vrclient.shutdown()

class VRobotClient:
    def __init__(self):
        self.vrnode_list = []

    def add_vrobot_node(self, vrnode: Any):
        self.vrnode_list.append(vrnode)

    def update(self):
        try:
            for vrnode in self.vrnode_list:
                vrnode.update()
        except Exception as e:
            print(Back.RED + f"[VRobotClient] Error in update: {e}" + Style.RESET_ALL)
            print(Fore.RED)
            traceback.print_exc()
            print(Fore.RED + Style.RESET_ALL)

    def shutdown(self):
        for vrnode in self.vrnode_list:
            vrnode.shutdown()


class VRobotNodeBase:
    def __init__(self, sysId:int = 0, max_states_history:int = 10, image_resolution: ImageResolution = ImageResolution.P720):
        try:
            self.first_ts = 0

            self.image_resolution = image_resolution
            self.sysId = sysId
            self.zenoh_node = ZenohNode(sysId)
            self.zenoh_node.create_publisher(f"vr/{self.sysId}/cmd")
            self.zenoh_node.create_subscriber(f"vr/{self.sysId}/states", self.states_listener)
            # states and image data can be stored here as needed max size = 10
            self.max_states_history = max_states_history
            self.states: List[VRobotState] = []

            # iox2 node for image subscriptions
            self.iox2_node = Iox2Node(sysId, 10)
            # self.iox2_node.create_image_subscriber("left", self.image_resolution)
            # self.iox2_node.create_image_subscriber("right", self.image_resolution)
            # self.iox2_node.create_image_subscriber("down", self.image_resolution)

            self.state = VRobotState()
            
            # self.imgStateLeft = get_image_state_type(self.image_resolution)()
            # self.imgStateRight = get_image_state_type(self.image_resolution)()
            # self.imgStateDown = get_image_state_type(self.image_resolution)()
            self.imgStates = dict()


            self.setup()
        except Exception as e:
            self.shutdown()
            print(Back.RED + f"[VRobotClient] Error in update: {e}" + Style.RESET_ALL)
            print(Fore.RED)
            traceback.print_exc()
            print(Fore.RED + Style.RESET_ALL)

    def setup(self):
        pass

    def register_img_subscriber(self, cam_side:str):
        self.iox2_node.create_image_subscriber(cam_side, self.image_resolution)
        self.imgStates[cam_side] = get_image_state_type(self.image_resolution)()
        return self.imgStates[cam_side]

        
    def states_listener(self, sample: any):
        try:
            topic: str = sample.key_expr
            payload: bytes = sample.payload.to_bytes()

            if StatesMsg.StatesMsgBufferHasIdentifier(payload, 0) is False:
                return
            
            statesMsgT = StatesMsgT.InitFromPackedBuf(payload, 0)
            
            # VRobotState = ubicoders' wrapper to pretty print
            states: VRobotState = VRobotState(statesMsgT)
            self.states.append(states)
            
            if len(self.states) > self.max_states_history:
                self.states.pop(0)


        except Exception as e:
            self.shutdown()
            print(f"[VRobotNode] Error in states_listener for sysId={self.sysId}: {e}")
        

    def read_new_states(self) -> bool:
        """
        If a newer state exists, update self.state and return True; else False.
        """
        try:
            if not self.states:
                return False
            latest = self.states[-1]
            if (self.first_ts == 0):
                self.first_ts = latest.timestamp
            
            if latest.timestamp > self.state.timestamp:
                self.state = latest
                return True
            return False
        except Exception as e:
            self.shutdown()
            print(f"[VRobotNode] Exception in read_new_states for sysId={self.sysId}:", flush=True)
            return False

    def read_new_image(self, cam_side:str) -> Tuple[bool]:
        img_state = self.iox2_node.get_image_data(cam_side, self.image_resolution)
        if img_state is None:
            return False
        if (img_state.ts > self.imgStates[cam_side].ts):
            self.imgStates[cam_side] = img_state
            return True
        return False


    def publish_cmd(self, cmd_data: bytes):
        self.zenoh_node.publish(f"vr/{self.sysId}/cmd", cmd_data)


    def shutdown(self):
        
        self.zenoh_node.shutdown()
        self.iox2_node.shutdown()