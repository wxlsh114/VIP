#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout,turnpage_play

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

    def exitClassroom(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n019:退出教室:等待老师期间退出教室----开始:'+now)
        login(self)
        sleep(2)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            print('本日暂时没有课程安排!')
            sleep(3)
        else:
            #driver.find_elements_by_class_name('XCUIElementTypeButton')[1].click()
            driver.find_element_by_accessibility_id('进入教室').click()
            sleep(5)
            another=driver.find_elements_by_accessibility_id('确定')
            if len(another)!=0:
                driver.find_element_by_accessibility_id('确定').click()
                sleep(5)
            #driver.find_element_by_accessibility_id('退出').click()
            #driver.find_elements_by_class_name('XCUIElementTypeButton')[2].click()
            TouchAction(self.driver).press(x=349,y=37).wait(100).release().perform()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_019b_afterExitClassroom_R.png'
            driver.save_screenshot(sf2)
            sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n019:退出教室:等待老师期间退出教室----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('exitClassroom'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_019b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(退出教室:等待老师期间退出教室)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
