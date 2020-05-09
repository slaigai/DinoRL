# URL to chrome dinosaur game
dino_url = 'chrome://dino'


def init_driver():
	# Search for chromedriver in current directory. Ignored by gitignore because each environment may have a different chrome driver.
	driver = webdriver.Chrome('./chromedriver')
	driver.set_window_position(0, 0)
	driver.set_window_size(500, 375) # minimum size for chrome window
	driver.get(dino_url)
	return driver


def screenshot_elem(elem):
	png = elem.screenshot_as_png
	img = Image.open(BytesIO(png))
	img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGBA2BGR)
	return img



if __name__ == "__main__":
	# Misc
	import time
	import numpy
	from watch import watch

	# Web driver
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	# Take screenshots using selenium
	# https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python

	# Image processing
	import cv2
	from PIL import Image
	from io import BytesIO

	# Initialize
	driver = init_driver()
	template = cv2.imread('templates/dino.png')

	try:
		# Wait for canvas to initialize, then wait for game animation
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, "runner-canvas"))
			)
		time.sleep(1)
		body = driver.find_element_by_tag_name('body')
		body.send_keys(Keys.SPACE)
		time.sleep(2)

		# Part of the screen to capture
		cv2.namedWindow('image', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('image', 500, 500)

		# Use "Runner.instance_" of javascript to access object
		# get score
		#     parseInt(Runner.instance_.distanceMeter.digits.join(''))
		# get high score
		#     parseInt(Runner.instance_.distanceMeter.highScore.slice(3).join(''))
		# is_game_over
		#     Runner.instance_.crashed

		watch({"top": 150, "left": 0, "width": 500, "height": 225})

	finally:
		driver.quit()


