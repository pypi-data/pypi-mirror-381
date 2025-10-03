import cv2
from .vrobot_node import VRobotNodeBase, vrobot_client_runner
from .rtg_pub import RTGPub

class VRobotNode(VRobotNodeBase):
    def __init__(self, sysId:int = 0):
        super().__init__(sysId)

    def setup(self):
        self.rtg = RTGPub(topic_name=f"vr/{self.sysId}/rtg")
        # self.state, self.imgStateLeft, self.imgStateRight, self.imgStateDown = self.initialize()
        cv2.namedWindow("CamLeft", cv2.WINDOW_NORMAL)    # make resizable window
        cv2.resizeWindow("CamLeft", 640, 360)
        cv2.namedWindow("CamRight", cv2.WINDOW_NORMAL)   # make resizable window
        cv2.resizeWindow("CamRight", 640, 360)
        cv2.namedWindow("CamDown", cv2.WINDOW_NORMAL)    # make resizable window
        cv2.resizeWindow("CamDown", 640, 360)

        self.register_img_subscriber("left")
        self.register_img_subscriber("right")
        self.register_img_subscriber("down")
        isNewState = self.read_new_states()
        self.start_time = self.state.timestamp if isNewState else 0
        print(f"Start time: {self.start_time}")

    def update(self):
        if self.read_new_states():
            ts = self.state.timestamp
            pos = self.state.linPos
            elapsed_sec = (ts - self.start_time) / 1000.0
            print(f"State t={elapsed_sec} pos=({pos.x:.2f},{pos.y:.2f},{pos.z:.2f})")
            self.rtg.publish(elapsed_sec, [pos.x, pos.y, pos.z])

        if self.read_new_image("left"):
            img = self.imgStates["left"].image_data
            # print(f"Image ts={self.imgStateLeft.ts}")
            cv2.imshow("CamLeft", img)
            cv2.waitKey(1)

        if self.read_new_image("right"):
            img = self.imgStates["right"].image_data    
            cv2.imshow("CamRight", img)
            cv2.waitKey(1)

        if self.read_new_image("down"):
            img = self.imgStates["down"].image_data
            cv2.imshow("CamDown", img)
            cv2.waitKey(1)
   


if __name__ == "__main__":
    try:
        vrobot_client_runner([VRobotNode(sysId=0)])
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down...")
    finally:
        cv2.destroyAllWindows()
        
