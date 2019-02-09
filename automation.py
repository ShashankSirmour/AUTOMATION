
from selenium import webdriver
import os
import time
from selenium.webdriver.common import action_chains, keys




os.environ["webdriver.chrome.driver"] = r"C:\Users\KIIT\chromedriver.exe"
noti = webdriver.ChromeOptions()
pref = {"profile.default_content_setting_values.notifications": 2}
noti.add_experimental_option("prefs", pref)

emailid = input("     enter id   :")
password = input("enter password : ")
numb = int(input("enter no of friend to send"))
fri = []
for i in range(numb):
    t = input("{}.  id  : ".format(i))
    fri.append(t)
massage = input("\n\n input your message : ")
stop = int(input("\ntime after which i will start sending the message "))

time.sleep(stop)
driver = webdriver.Chrome(
    chrome_options=noti, executable_path=r"C:\Users\KIIT\chromedriver.exe")


driver.maximize_window()
driver.get("http://facebook.com/")
driver.implicitly_wait(10)
e = driver.find_element_by_xpath('//input[@id="email"]')
p = driver.find_element_by_xpath('//input[@id="pass"]')
c = driver.find_element_by_xpath('//label[@id="loginbutton"]/input')

e.send_keys(emailid)
p.send_keys(password)
c.click()
for i in fri:
    driver.get(r"https://www.facebook.com/messages/t/"+i)
    driver.implicitly_wait(10)

    for i in range(10):

        cc = action_chains.ActionChains(driver)
        cc.send_keys(massage+keys.Keys.ENTER)
        cc.perform()

driver.quit()
