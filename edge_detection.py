import numpy as np
import cv2
import pygame



class EdgeDetect:
    video = cv2.VideoCapture('res\Test Peter high light no hit.mp4')
    frame_no = 375
    last_frame = pygame.time.get_ticks()

    video.set(1, 375)

    def main(self):
        '''
        start = pygame.time.get_ticks()
        delta_time = (start - EdgeDetect.last_frame) / 50
        EdgeDetect.last_frame = start
        EdgeDetect.frame_no = EdgeDetect.frame_no + delta_time
        EdgeDetect.video.set(1, EdgeDetect.frame_no)
        '''

        ret, frame = EdgeDetect.video.read()

        frame = frame[0:700, 50:1200]

        # Flip video frame by frame
        #frame = cv2.flip(frame, 1)

        frame = np.rot90(frame)

        canny = cv2.Canny(frame, 50, 128)

        #canny = cv2.medianBlur(canny, 1)

        return canny
