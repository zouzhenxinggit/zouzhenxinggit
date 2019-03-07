#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.renren.com")

driver.find_element_by_name("email").send_keys("15145100618")
driver.find_element_by_name("password").send_keys("zouge666666")

driver.find_element_by_id('login').click()

time.sleep(2)
print driver.save_screenshot("renren.png")


key = raw_input("请输入验证码:")
key1 = key.decode('utf-8')
print key1
driver.find_element_by_name("icode").send_keys(key1)

driver.find_element_by_id('login').click()

time.sleep(2)
print driver.save_screenshot("renrenlogin.png")

