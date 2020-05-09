import time

import cv2
import mss
import numpy
from progressbar import progressbar


def find_template(img, template):
    h, w, _ = template.shape

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right


def mark_template(img, template):
    top_left, bottom_right = find_template(img, template)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)


def mark_dino(img, dino_template):
    dino_region = {'left': 0, 'right': 150, 'top': 0, 'bottom': 450}
    img_cropped = img[dino_region['top']:dino_region['bottom'] + 1, dino_region['left']:dino_region['right'] + 1, :]
    top_left, bottom_right = find_template(img_cropped, dino_template)
    top_left = (top_left[0] + dino_region['left'], top_left[1] + dino_region['top'])
    bottom_right = (bottom_right[0] + dino_region['left'], bottom_right[1] + dino_region['top'])
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)


def watch(monitor):
    pb = progressbar(min=0, max=60, bar_size=25)
    dino_template = cv2.imread('templates/dino.png')
    with mss.mss() as sct:
        # Part of the screen to capture
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 500,500)

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            frame = numpy.array(sct.grab(monitor))
            img = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
            mark_dino(img, dino_template)
            # mark_template(img, dino_template)

            # Display the picture
            cv2.imshow("image", img)

            # Print fps
            fps = 1 / (time.time() - last_time)
            pb.print_progress(fps)

            # Press "q" to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                print()
                break

if __name__ == "__main__":
    monitor = {"top": 300, "left": 0, "width": 500, "height": 450}
    watch(monitor)
    # progress bar in loop, sleep 0.5 seconds, 100 increments, max of 100, carriage return \r