#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher_ios933 import login,logout

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
        sleep(2)


    def testDevice(self):
        driver=self.driver
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n008:设备检测----开始:'+now)
        login(self)
        sleep(3)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_008b_pCenter_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('设备检测').click()
        sleep(2)
        #test now
        driver.find_element_by_accessibility_id('开始测试').click()
        sleep(2)
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
        if driver.find_element_by_accessibility_id('检测通过'):
            print('\n检测通过')
        else:
            print('\n检测未通过')
        sleep(2)
        driver.swipe(500,500,0,-180,1000)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n008:设备检测----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('testDevice'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_008b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(设备检测)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
