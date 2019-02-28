#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout

class TestStudent(unittest.TestCase):

    def setUp(self):
        # set up appium
        desired_caps = {}
        #desired_caps['appium-version'] = '1.7.1'
        desired_caps['platformName'] = 'iOS'
        desired_caps['browserName']=''
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '11.0'
        desired_caps['deviceName'] = 'iPhone6'
        desired_caps['app'] = os.path.abspath('../VIPStudent.ipa')
        desired_caps['udid'] = '851c908fafaa15e592e2145131cc202cd20cc977'
        desired_caps['fullReset'] = True
        desired_caps['clearSystemFiles'] = True
        desired_caps['xcodeOrgId'] = 'P2ZL3LJVPZ'
        #desired_caps['xcodeSigning'] = 'iPhone Developer'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #self.driver.implicitly_wait(30)
        sleep(2)

    def generalSetting(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n011:通用设置----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_011b_personCenter_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('通用设置').click()
        sleep(2)
        #上传日志
        driver.find_element_by_accessibility_id('上传日志').click()
        sleep(5)
        #清除缓存
        driver.find_element_by_accessibility_id('清空缓存').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf4='./'+now+'_011b_clearCache_R.png'
        driver.save_screenshot(sf4)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.swipe(800,500,0,-220,500)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n011:通用设置----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('generalSetting'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_011b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(通用设置)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
