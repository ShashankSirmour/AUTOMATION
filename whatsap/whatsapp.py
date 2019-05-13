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








