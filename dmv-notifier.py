from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from playsound import playsound
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://nyrtspublicsite.azurewebsites.net")
print(driver.title)

ID = driver.find_element_by_name("ClientId")
ID.send_keys("806454516")
ID.send_keys(Keys.TAB)

MONTH = driver.find_element_by_id("monthDropdown")
MONTH.send_keys("August")
MONTH.send_keys(Keys.TAB)

DAY = driver.find_element_by_id("dayDropdown")
DAY.send_keys("6")
DAY.send_keys(Keys.TAB)

YEAR = driver.find_element_by_id("yearDropDown")
YEAR.send_keys("2002")
YEAR.send_keys(Keys.ENTER)
YEAR.send_keys(Keys.ENTER)

time.sleep(10)

print(driver.title)

driver.implicitly_wait(30)
APPOINTMENT = driver.find_element_by_class_name("btn-default-bar").click()
print(driver.title)


driver.implicitly_wait(10)

date = driver.find_element_by_xpath("//*[@id='target']/div[2]/div[3]").text
print(date)
if "Jul" in date: print("NOPE")
while "Jul" in date:
    driver.refresh()
    .
if "Jun" in date playsound('/path/note.wav')
    
print(date)
print(driver.title)
    
