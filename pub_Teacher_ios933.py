#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
#from HTMLTestRunner import HTMLTestRunner
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction

def login(self):
    driver=self.driver
    sleep(2)
    driver.find_element_by_accessibility_id('好').click()
    sleep(1)
    """
    driver.swipe(350,500,-320,0,1000)
    sleep(1)
    driver.swipe(350,500,-320,0,1000)
    sleep(1)
    driver.find_element_by_accessibility_id('马 上 体 验').click()
    sleep(1)
    """
    #跳 过
    driver.find_elements_by_accessibility_id('跳 过')[1].click()
    sleep(1)
    mo=driver.find_element_by_class_name('XCUIElementTypeTextField')
    mo.click()
    #18311111111
    mo.set_value('18311111111')
    #driver.find_element_by_accessibility_id('完成').click()
    TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
    sleep(1)
    pwd=driver.find_element_by_class_name('XCUIElementTypeSecureTextField')
    pwd.click()
    pwd.set_value('123456')
    #driver.find_element_by_accessibility_id('完成').click()
    TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
    sleep(1)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="登录"]').click()
    sleep(4)
    #someone already logged in
    another=driver.find_elements_by_accessibility_id('确定')
    if len(another)!=0:
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
    o=driver.find_elements_by_accessibility_id('好')
    if len(o)!=0:
        driver.find_element_by_accessibility_id('好').click()
        sleep(2)
    #test now
    driver.find_element_by_accessibility_id('开始测试').click()
    sleep(3)
    driver.find_element_by_accessibility_id('点击开始录音').click()
    sleep(3)
    driver.find_element_by_accessibility_id('停止录音').click()
    sleep(2)
    driver.find_element_by_accessibility_id('有听到声音').click()
    sleep(2)
    driver.find_element_by_accessibility_id('下一步').click()
    sleep(2)
    driver.find_element_by_accessibility_id('下一步').click()
    sleep(2)
    driver.find_element_by_accessibility_id('完成测试').click()
    sleep(3)

def logout(self):
    driver=self.driver
    driver.find_element_by_accessibility_id('个人中心').click()
    sleep(2)
    driver.swipe(500,500,0,-250,1000)
    sleep(2)
    driver.find_element_by_accessibility_id('退出登录').click()
    sleep(2)
    driver.find_element_by_accessibility_id('确定').click()
    sleep(2)

def turnpage_play(self):
    driver=self.driver
    #turn page left/right
    """
    driver.swipe(350,500,-320,0,1000)
    sleep(1)
    driver.swipe(30,500,320,0,1000)
    sleep(1)
    """
    pagelist=driver.find_elements_by_accessibility_id('ic next1')
    if len(pagelist)!=0:
        driver.find_elements_by_accessibility_id('ic next1')[0].click()
        sleep(1)
        driver.find_elements_by_accessibility_id('ic previous')[0].click()
        sleep(1)
    #Add play code here
    p=driver.find_elements_by_accessibility_id('ic play2')
    if len(p)!=0:
        driver.find_element_by_accessibility_id('ic play2').click()
        sleep(8)
        driver.find_element_by_accessibility_id('ic play2').click()
        sleep(2)
    sleep(1)
