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

    def bottomClassSheet(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n015:课后陪练单----开始:'+now)
        login(self)
        sleep(2)
        #bottom classSheet
        driver.find_element_by_accessibility_id('陪练单').click()
        sleep(2)
        driver.find_element_by_accessibility_id('查看陪练单').click()
        sleep(6)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_015b_classSheetBottomTop_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.swipe(800,500,0,-400,500)
        sleep(2)
        driver.swipe(800,500,0,-400,500)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_015b_classSheetBottomTail_R.png'
        driver.get_screenshot_as_file(sf1)
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
        print('\n015:课后陪练单----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('bottomClassSheet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_015b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(课后陪练单)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
