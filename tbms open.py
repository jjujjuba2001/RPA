import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


id = 'hwjung@inzisoft.com'
pw = 'nara0805~!'

lable = ['팀원', '팀장', '대표이사', '근태 담당자', '관리자']           # 권한별 계정 리스트에 담기

driver = webdriver.Chrome()
Options = Options()
Options.add_experimental_option("detach", True)

driver.get("https://tbms.mobileleader.com:8010/login")                 # TBMS 사이트 접속
driver.maximize_window()
Options.add_experimental_option("excludeSwitches", ["enable-automation"])     # 자동화 제어 알림 줄 삭제 , 하지만 안됨
driver.implicitly_wait(5)
print (driver.current_window_handle)

sdkid = driver.find_element(By.XPATH, '//*[@id="plainUserId"]')               
sdkid.send_keys(id)                                                             # id 입력
time.sleep(2)

#sdkpw = driver.find_element(By.XPATH, '//*[@id="plainUserPw"]')
driver.find_element(By.XPATH, '//*[@id="plainUserPw"]').send_keys(pw)           # pw 입력
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/a').click()      # 로그인 버튼 클릭
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="lnb"]/ul/li[7]/a').click()    #휴가 탭 생성시, xpath 변경 해야함
time.sleep(3)

path = r'C:\Users\user\Desktop\TBMS SCREEN SHOT'                     # 저장할 스크린 샷 경로
for i in lable:                                                      # 권한별 스크린 샷 저장하기   
    filename = path + '\chrome '+ i + '.png'
    driver.save_screenshot(filename)


'''driver.switch_to.window(driver.window_handles[1])
print (driver.current_window_handle)

driver.implicitly_wait(5)
s_element = driver.find_element(By.ID, "nation")
time.sleep(2)
#driver.get_screenshot_as_png("스샷.png")

driver.save_screenshot(r"C:\doit\스샷.png")
#s_element.save(r"C:\doit\스샷.png")
'''