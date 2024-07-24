import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()

driver.get("https://www.naver.com")
driver.maximize_window()
driver.implicitly_wait(5)


print (driver.current_window_handle)
driver.find_element(By.CLASS_NAME, "DailyBoardView-module__header_title___Uk3ix").click()
driver.implicitly_wait(5)

driver.switch_to.window(driver.window_handles[1])
print (driver.current_window_handle)

driver.implicitly_wait(5)
s_element = driver.find_element(By.ID, "nation")
time.sleep(2)
#driver.get_screenshot_as_png("스샷.png")

driver.save_screenshot(r"C:\doit\스샷.png")
#s_element.save(r"C:\doit\스샷.png")
