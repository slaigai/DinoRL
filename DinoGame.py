# Misc
import time
import cv2
import mss
import numpy
from drivertools import *

# Web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


class DinoGame(object):
    def __init__(self):
        self.driver = None
        self.window_x = None
        self.window_y = None
        self.window_width = None
        self.window_height = None
        self.inner_x = None
        self.inner_y = None
        self.inner_width = None
        self.inner_height = None

    def __enter__(self):
        self.init_driver()
        self.update_position()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
        self.driver.quit()
        print("Exited")

    def init_driver(self, dino_url="chrome://dino", chrome_driver_path="./chromedriver"):
        print("Initializing")
        # Default to chromedriver in current directory. Ignored by gitignore because each environment may have a
        # different chrome driver.
        driver = webdriver.Chrome(chrome_driver_path)
        driver.set_window_position(0, 0)
        driver.set_window_size(500, 375)  # minimum size for chrome window
        driver.get(dino_url)

        # Wait for canvas to initialize
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "runner-canvas"))
        )
        # Wait for page body to render
        time.sleep(1)
        # Start dino game by pressing space
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.SPACE)
        # Wait for intro animation to complete (roughly 1.5 seconds, 2 seconds to be safe)
        time.sleep(2)

        self.driver = driver

    def update_position(self):
        self.window_x, self.window_y, self.window_width, self.window_height = get_window_position(self.driver)
        self.inner_x, self.inner_y, self.inner_width, self.inner_height = get_inner_position(self.driver)

    def watch(self):
        dino_template = cv2.imread('templates/dino.png')
        monitor = {"top": self.inner_y, "left": self.inner_x, "width": self.inner_width, "height": self.inner_height}
        with mss.mss() as sct:
            # Part of the screen to capture
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('image', self.window_width, self.window_height)

            time_since_print = 0
            while "Screen capturing":
                last_time = time.time()

                # Find and screenshot game
                frame = numpy.array(sct.grab(monitor))
                img = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
                mark_dino(img, dino_template)

                # Display the picture
                cv2.imshow("image", img)

                # Press "q" to quit
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    print()
                    break

                # Print fps
                elapsed_time = time.time() - last_time
                fps = 1 / elapsed_time
                time_since_print += elapsed_time
                # Print game status every 1 second
                if time_since_print >= 1:
                    print(f"""
FPS: {int(fps)}
Game over: {self.is_crashed}
Score: {self.score}
High Score: {self.high_score}""")
                    time_since_print = 0

    @property
    def score(self):
        return self.driver.execute_script("return parseInt(Runner.instance_.distanceMeter.digits.join(''))")

    @property
    def is_crashed(self):
        return self.driver.execute_script("return window.Runner.instance_.crashed")

    @property
    def high_score(self):
        return self.driver.execute_script("return parseInt(Runner.instance_.distanceMeter.highScore.slice(3).join("
                                           "''))")


if __name__ == "__main__":
    with DinoGame() as game:
        print("Initialized")
        game.watch()





