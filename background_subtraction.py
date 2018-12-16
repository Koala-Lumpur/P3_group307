import numpy as np
import cv2


class BackSub:
    video = cv2.VideoCapture('res/test 12.mp4')
    back_frame = cv2.imread('res/test 12.jpg')
    frame_no = 60
    video.set(1, frame_no)

    def main(self):
        ret, frame = BackSub.video.read()
        mask = cv2.subtract(frame, BackSub.back_frame)
        mask2 = cv2.subtract(BackSub.back_frame, frame)
        mask = cv2.add(mask, mask2)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(mask, 40, 255, cv2.THRESH_BINARY)
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