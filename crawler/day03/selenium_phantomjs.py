#!/usr/bin/python
#coding=utf-8

# Selenium是一个Web的自动化测试工具 + 无界面(headless)浏览器
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dirver = webdriver.PhantomJS()
dirver.get("http://www.baidu.com")
print dirver.save_screenshot("baidu1.png")

dirver.find_element_by_id("kw").send_keys(u"美女")
print dirver.save_screenshot("baidu2.png")

dirver.find_element_by_id("su").click()
print dirver.save_screenshot("baidu3.png")

data = dirver.find_element_by_id("wrapper").text
print data

# # 打印数据内容
# print data

# # 打印网页渲染后的源代码
# print dirver.page_source

# # 获取当前页面Cookie
# print dirver.get_cookies()

# # 获取当前url
# print dirver.current_url

# # 关闭当前页面，如果只有一个页面，会关闭浏览器
# # dirver.close()

# # 关闭浏览器
# dirver.quit()