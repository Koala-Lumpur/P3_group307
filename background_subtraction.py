import numpy as np
import cv2
import pygame

class BackSub:
    video = cv2.VideoCapture('res\Test Peter high light no hit.mp4')
    back_frame = cv2.imread('res\Background picture Peter high light no hit.jpg')
    #back_frame = np.rot90(back_frame)
    #back_frame = cv2.cvtColor(back_frame, cv2.COLOR_BGR2GRAY)7
    frame_no = 375

    def main(self):
        # Capture video
        BackSub.video.set(1, BackSub.frame_no)
        ret, frame = BackSub.video.read()
        #print(frame.shape[1])

        # Flip video frame by frame
        #frame = np.rot90(frame)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mask = cv2.subtract(frame, BackSub.back_frame)
        mask2 = cv2.subtract(BackSub.back_frame, frame)
        mask = cv2.add(mask, mask2)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(mask, 40, 255, cv2.THRESH_BINARY)
        #thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)
        thresh1 = cv2.medianBlur(thresh1, 9)
        thresh1 = np.rot90(thresh1)

        return thresh1


'''
while True:
    cv2.imshow('meh', main())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
'''

'''
# Show the video
cv2.imshow('frame', frame)
cv2.imshow('first frame', back_frame)
cv2.imshow('ref_image', ref_image)
cv2.imshow('mask', mask)
cv2.imshow('threshold', thresh1)
'''