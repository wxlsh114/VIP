#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher_ios933 import login,logout,turnpage_play

class TestTeacher(unittest.TestCase):

    def setUp(self):
        # set up appium
        desired_caps = {}
        #desired_caps['appium-version'] = '1.6.5'
        desired_caps['platformName'] = 'iOS'
        desired_caps['browserName']=''
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone5s'
        desired_caps['app'] = os.path.abspath('../Text-Vip-Gangqin-Teacher.ipa')
        desired_caps['udid'] = 'e99cdf92c6f685360fe31ecf6ece48fe63150daa'
        desired_caps['fullReset'] = True
        desired_caps['clearSystemFiles'] = True
        desired_caps['xcodeOrgId'] = 'P2ZL3LJVPZ'
        desired_caps['xcodeSigning'] = 'iPhone Developer'
        #desired_caps['autoAcceptAlerts'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #self.driver.implicitly_wait(30)
        sleep(3)


    def bottomClassshet(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n015:底部陪练单----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_accessibility_id('陪练单').click()
        sleep(3)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_015b_unSentClassSheetB_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('编辑陪练单').click()
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_015b_unSentClassSheetDetailTop_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        driver.swipe(500,500,0,-400,1000)
        sleep(1)
        driver.swipe(500,500,0,-400,1000)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_015b_unSentClassSheetDetailTail_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('已发送陪练单').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_015b_sentClassSheetB_R.png'
        driver.get_screenshot_as_file(sf)
        sleep(2)
        driver.find_element_by_accessibility_id('查看陪练单').click()
        sleep(10)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_015b_sentClassSheetDetailTop_R.png'
        driver.save_screenshot(sf3)
        sleep(2)
        driver.swipe(500,500,0,-400,1000)
        sleep(1)
        driver.swipe(500,500,0,-400,1000)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf4='./'+now+'_015b_sentClassSheetDetailTail_R.png'
        driver.save_screenshot(sf4)
        sleep(2)
        p=driver.find_elements_by_accessibility_id('点击播放语音评价')
        if len(p)!=0:
            driver.find_element_by_accessibility_id('点击播放语音评价').click()
            sleep(6)
            driver.find_element_by_accessibility_id('点击播放语音评价').click()
            sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n015:底部陪练单----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('bottomClassshet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_015b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOSiOS9.3.3/iPhone5s真机(底部陪练单)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
