#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction


def login(self):
    driver=self.driver
    sleep(2)
    #1080*1920 5.2''
    #跳 过
    driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
    #driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnSkip').click()
    sleep(2)
    #driver.find_find_element_by_android_uiautomator('马上体验').click()
    #sleep(4)
    user=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etUserName')
    user.click()
    user.set_value('13923121234')
    sleep(1)
    pwd=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etPassword')
    pwd.click()
    pwd.set_value('123456')
    sleep(1)
    #登录
    driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnLogin').click()
    sleep(4)
    driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
    sleep(2)
    #test now
    driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("停止录音")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("有听到声音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("您已完成测试")').click()
    sleep(3)

def logout(self):
    driver=self.driver
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    sleep(2)
    driver.swipe(1000,1600,1000,1250,1000)
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
    sleep(2)

def testdevice(self):
    driver=self.driver 
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    sleep(2)
    t=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvState').text
    print(t)
    assert '测试已通过' in t
    sleep(2)
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    sf='./'+now+'_deviceTest_R.png'
    driver.save_screenshot(sf)
    sleep(2)
    driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvState').click()
    sleep(3)
    #test now
    driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
    sleep(3)
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
    driver.find_element_by_android_uiautomator('new UiSelector().text("您已完成测试")').click()
    sleep(3)

def turnpage_play(self):
    driver=self.driver
    #turn page left/right
    page=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivNext')
    if len(page)!=0:
        driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivNext')[0].click()
        sleep(2)
        driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivLast')[0].click()
        sleep(2)
    sleep(1)
    #Add play code here
    pb=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnPlayUrl')
    if len(pb)!=0:
        driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnPlayUrl').click()
        sleep(8)
        driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnPlayUrl').click()
        sleep(2)
    sleep(1)
