import numpy as np
import cv2


class BackSub:

    video = cv2.VideoCapture(0);
    first = True
    global back_frame

    def cap_frame(self):
        _, back_frame = BackSub.video.read()
        back_frame = np.rot90(back_frame)
        back_frame = cv2.cvtColor(back_frame, cv2.COLOR_BGR2GRAY)
        return back_frame

    def main(self):

        if BackSub.first:
            global back_frame
            back_frame = BackSub.cap_frame(self)
            BackSub.first = False

        # Capture video
        ret, frame = BackSub.video.read()

        # Flip video frame by frame
        frame = np.rot90(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mask = cv2.subtract(back_frame, frame)
        ret, thresh1 = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)
        #thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)
        thresh1 = cv2.medianBlur(thresh1, 9)

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