


if __name__ == "__main__":
	# URL to chrome dinosaur game
	dino_url = 'chrome://dino'

	# Open new chrom window if chrome is not yet open. Opens tab if chrome is already open. Try selenium instead
	# import webbrowser
	# webbrowser.open_new(dino_url)

	# Misc
	import time
	import re
	import numpy
	from progressbar import progressbar

	# Web driver
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC

	# Image processing
	import cv2
	from PIL import Image
	from io import BytesIO

	# Search for chromedriver in current directory. Ignored by gitignore because each environment may have a different chrome driver.
	# driver = webdriver.Chrome('./chromedriver')
	# driver.set_window_position(0, 0)
	# driver.set_window_size(500, 500)
	# driver.get(dino_url)

	# Take screenshots using selenium
	# https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python

	try:
		# element = WebDriverWait(driver, 10).until(
		# 	EC.presence_of_element_located((By.CLASS_NAME, "runner-canvas"))
		# 	)
		# time.sleep(1)
		# body = driver.find_element_by_tag_name('body')
		# body.send_keys(Keys.SPACE)
		# time.sleep(2)
		#
		# # Part of the screen to capture
		# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
		# cv2.resizeWindow('image', 500, 500)
		#
		# png = body.screenshot_as_png
		# print(type(png))
		# img = Image.open(BytesIO(png))
		# print(type(img))
		# opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGBA2GRAY)
		# print(type(opencvImage))
		# cv2.imwrite('game.png', opencvImage)

		img = cv2.imread('game.png')
		template = cv2.imread('templates/dino.png')
		print(template.shape)
		h, w, _ = template.shape

		res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		top_left = max_loc
		bottom_right = (top_left[0] + w, top_left[1] + h)
		cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

		cv2.imshow("image", img)

		while "Screen capturing":
			# Press "q" to quit
			if cv2.waitKey(25) & 0xFF == ord("q"):
				cv2.destroyAllWindows()
				print()
				break

	# im = Image.open(BytesIO(png))
	# im.show()
	finally:
		# driver.quit()
		pass

# elem = driver.find_element_by_tag_name('body')
# elem.send_keys(Keys.SPACE)




