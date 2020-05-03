import time

import cv2
import mss
import numpy
from progressbar import progressbar

def watch(monitor):
    pb = progressbar(min=0, max=60, bar_size=25)
    with mss.mss() as sct:
        # Part of the screen to capture
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 500,500)

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))

            # Display the picture
            cv2.imshow("image", img)

            # Print fps
            fps = 1 / (time.time() - last_time)
            pb.print_progress(fps)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                print()
                break

if __name__ == "__main__":
    monitor = {"top": 0, "left": 0, "width": 500, "height": 500}
    watch(monitor)
    # progress bar in loop, sleep 0.5 seconds, 100 increments, max of 100, carriage return \r