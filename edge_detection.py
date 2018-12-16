import numpy as np
import cv2


class EdgeDetect:
    video = cv2.VideoCapture('res/test 12.mp4')
    frame_no = 60
    video.set(1, frame_no)

    def main(self):
        ret, frame = EdgeDetect.video.read()
        frame = frame[0:675, 0:1200]
        frame = np.rot90(frame)
        canny = cv2.Canny(frame, 50, 128)
        return canny
