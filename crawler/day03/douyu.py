#!/usr/bin/python
#coding=utf-8

# python的测试模块
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    # #具体的测试用例方法，一定要以test开头
    def testDouyu(self):
        self.driver.get('http://www.douyu.com/directory')
        # 时间紧
        # http://www.douyu.com/directory/all
        
        # print self.driver.save_screenshot("douyu.png")
        # 指定xml解析
        soup = BeautifulSoup(self.driver.page_source, 'xml')
        game = soup.find_all('strong')
        for m in game:
            print m

    # # 退出时的清理方法
    def tearDown(self):
        print '加载完成...'
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()