from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time
from selenium.webdriver.common import action_chains, keys
os.environ["webdriver.chrome.driver"] = r"C:\Users\KIIT\chromedriver.exe"
noti = webdriver.ChromeOptions()
pref = {"profile.default_content_setting_values.notifications": 2}
noti.add_experimental_option("prefs", pref)
driver = webdriver.Chrome(
    chrome_options=noti, executable_path=r"C:\Users\KIIT\chromedriver.exe")
driver.maximize_window()

driver.get("https://web.whatsapp.com/")

#vari=['bhut khub','wah wah ',' randi jat ka orignal chhkka','jhat ke bal ','chutiye','madarchod ','tere gand me kide pade ',"chut ke sodage","gand chhattu","sn mishra ki jhatt"]

while(1):
    a = input("input your prosess : ")
    if a == "start":
        break
b = int(input("MESSAGE loop : "))
c = input("message : ")
# c=list()
# for i in range(b):
#     temp=input(" {} entry ".format(i))
#     c.append()

action = action_chains.ActionChains(driver)

action.send_keys(keys.Keys.TAB+keys.Keys.ENTER).perform()

for i in range(b):
    ac = action_chains.ActionChains(driver)
    ac.send_keys(c+keys.Keys.ENTER).perform()
"""


action=action_chains.ActionChains(driver)
driver.implicitly_wait(10)
time.sleep(2)
inid=driver.find_element(By.XPATH,'//input[@id="u_0_j"]')
inid.send_keys("lovelyray")
time.sleep(2)
action.send_keys(keys.Keys.TAB + "localtest" + keys.Keys.TAB +
                 "ekodiadddjfdhkjdddjfkdhghzhjkkdmail@email.com" + keys.Keys.TAB +
                 "ekodiadddjfdhkjdddjfkdhghzhjkkdmail@email.com" + keys.Keys.TAB +
                 "786786121@saM" + keys.Keys.TAB + keys.Keys.ARROW_UP +
                 keys.Keys.TAB + keys.Keys.ARROW_DOWN + keys.Keys.TAB +
                 keys.Keys.ARROW_DOWN * 10 + keys.Keys.TAB + keys.Keys.TAB +
                 keys.Keys.ARROW_DOWN).perform()

driver.find_element(By.XPATH, '//button[@id="u_0_11"]').click()

try:
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '(//*[@id="u_0_i"]//a)[2]').click()
    driver.find_element(By.XPATH,'//a[@id="u_fetchstream_3_8"]').click()
    driver.get('https://www.facebook.com/photo.php?fbid=1712795185483741&set=a.355123374584269.83416.100002598295944&type=3&theater')
    driver.find_element(By.XPATH,'//div[@id="fbPhotoSnowliftFeedback"]//a').click()
except :
    driver.get('https://www.facebook.com/photo.php?fbid=1712795185483741&set=a.355123374584269.83416.100002598295944&type=3&theater')
    driver.find_element(By.XPATH,'//div[@id="fbPhotoSnowliftFeedback"]//a').click()
"""
