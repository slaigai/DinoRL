# URL to chrome dinosaur game
dino_url = 'chrome://dino'

# Open new chrom window if chrome is not yet open. Opens tab if chrome is already open. Try selenium instead
# import webbrowser
# webbrowser.open_new(dino_url)

from selenium import webdriver

# Search for chromedriver in current directory. Ignored by gitignore because each environment may have a different chrome driver.
driver = webdriver.Chrome('./chromedriver')
driver.set_window_position(0, 0)
driver.set_window_size(500, 500)
driver.get(dino_url)
