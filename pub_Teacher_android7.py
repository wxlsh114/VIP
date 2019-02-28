#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction


def login(self):
    #1080*1920
    driver=self.driver
    sleep(3)
    """
    driver.swipe(1000,1600,50,1600,1000)
    sleep(1)
    driver.swipe(1000,1600,50,1600,1000)
    sleep(1)
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnStart').click()
    sleep(2)
    #driver.find_find_element_by_android_uiautomator('马上体验').click()
    #sleep(4)
    """
    #跳 过
    #driver.find_element_by_android_uiautomator('new UiSelector().text("跳 过")').click()
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnSkip').click()
    sleep(2)
    user=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/etUserName')
    user.click()
    user.set_value('18923236756')
    sleep(1)
    pwd=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/etPassword')
    pwd.click()
    pwd.set_value('123456')
    sleep(1)
    #登录
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnLogin').click()
    sleep(4)
    driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
    sleep(2)
    
    #test now
    driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
    sleep(4)
    driver.find_element_by_android_uiautomator('new UiSelector().text("停止录音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("有听到声音")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("完成测试")').click()
    sleep(3)
    #someone already logged in
    another=driver.find_elements_by_android_uiautomator('new UiSelector().text("确定")')
    if len(another)!=0:
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        sleep(3)


def logout(self):
    driver=self.driver
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    sleep(3)
    driver.swipe(1000,1600,1000,1100,1000)
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
    sleep(2)


def testdevice(self):
    driver=self.driver 
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    sleep(2)
    t=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/testingHintTv').text
    print(t)
    assert '测试已通过' in t
    sleep(2)
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/testingHintTv').click()
    sleep(2)
    #test now
    driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("停止录音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("有听到声音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("完成测试")').click()
    sleep(3)

def turnpage_play(self):
    driver=self.driver
    pagelist=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/nextYuePuIv')
    #print(str(len(pagelist)))
    if len(pagelist)!=0:
        driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/nextYuePuIv')[0].click()
        sleep(1)
        driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/lastYuePuIv')[0].click()
        sleep(1)
    #Add play code here
    pb=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/btnPlayUrl')
    if len(pb)!=0:
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnPlayUrl').click()
        sleep(8)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnPlayUrl').click()
        sleep(2)
