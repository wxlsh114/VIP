#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
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

    def waitForTeacher(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:等待老师进入（学生进入，老师未进入）---开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_accessibility_id('进入教室').click()
        sleep(5)
        another=driver.find_elements_by_accessibility_id('确定')
        if len(another)!=0:
            driver.find_element_by_accessibility_id('确定').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_002b_enteredClassroom_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        f1=driver.find_elements_by_accessibility_id('pic_wait')
        if len(f1)!=0:
            print('\nThere is a sign:请等待老师进入教室')
            sleep(2)
        driver.find_element_by_accessibility_id('呼叫老师').click()
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_002b_afterCallTeacher_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        #driver.find_element_by_accessibility_id('退出').click()
        #driver.find_elements_by_class_name('XCUIElementTypeButton')[1].click()
        TouchAction(self.driver).press(x=349,y=37).wait(100).release().perform()
        sleep(4)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:等待老师进入（学生进入，老师未进入）----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('waitForTeacher'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_002b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(等待老师进入（学生进入，老师未进入）)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
