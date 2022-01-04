# DMV-Notifier

![alt text](https://github.com/francosae/DMV-Checker/blob/main/webpage.PNG)


## What does it do?

This script loads the New York DMV Website and automatically fills out user's ID Number, and full birth date. After filling out the information, it waits for the following page to load. After the list of available appointments its displayed, it will search the for the element which displays the month the appointments are for; if no appointment has the desired month, it will continually refresh the page. Once an appointment is found that has the desired month, a sound will play- notifying you that an appointment is available. 


## Usage
Use pip to install selenium
```
pip install selenium
```

You will need to replace the ID, Month, Day, and Year to fit your information. Additionally, you will also need to replace the months that are searched for with months you wish to have the appointment for and months that are not desired.
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from playsound import playsound
from webdriver_manager.chrome import ChromeDriverManager

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://nyrtspublicsite.azurewebsites.net")
print(driver.title)

#Replace ID, Month, Day with your own information.
ID = driver.find_element_by_name("ClientId")
ID.send_keys("ID")
ID.send_keys(Keys.TAB)

MONTH = driver.find_element_by_id("monthDropdown")
MONTH.send_keys("MONTH")
MONTH.send_keys(Keys.TAB)

DAY = driver.find_element_by_id("dayDropdown")
DAY.send_keys("DAY")
DAY.send_keys(Keys.TAB)


YEAR = driver.find_element_by_id("yearDropDown")
YEAR.send_keys("BIRTH YEAR")
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

#Replace "Jul" with 1 month ahead of your current one. If you are looking for appointments in September put "Oct" for October.
if "Jul" in date: print("NOPE")
while "Jul" in date:
    driver.refresh()

#Replace "Jun" with the current month you are in. If you are in September, put "Sep"
if "Jun" in date playsound('/path/note.wav')
    
print(date)
print(driver.title)
```

## Roadmap

- This is fairly small and I would like to expand on this in the future by making automatic appointment scheduling possible.
