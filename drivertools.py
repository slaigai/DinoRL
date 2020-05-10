def get_window_position(driver):
    window_x = driver.execute_script("return window.screenX")
    window_y = driver.execute_script("return window.screenY")
    window_width = driver.execute_script("return window.outerWidth")
    window_height = driver.execute_script("return window.outerHeight")
    return window_x, window_y, window_width, window_height


def get_inner_position(driver):
    window_x, window_y, window_width, window_height = get_window_position(driver)
    inner_x = window_x + driver.execute_script("return window.outerWidth - window.innerWidth")
    inner_y = window_y + driver.execute_script("return window.outerHeight - window.innerHeight")
    inner_width = driver.execute_script("return window.innerWidth")
    inner_height = driver.execute_script("return window.innerHeight")
    return inner_x, inner_y, inner_width, inner_height
