#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestStudent(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'PRA-AL00'
        #desired_caps['udid'] = 'HMKNW17225011700'
        desired_caps['app'] = PATH('../VIPStudent_2.0.4.apk')
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass.pnlclass_student.ceshi'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def waitForTeacher(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:等待老师进入（学生进入，老师未进入）----开始:'+now)
        login(self)
        sleep(2)
        lis1=driver.find_elements_by_android_uiautomator('new UiSelector().text("课程表")')
        if len(lis1)==0:
            print('本周暂时没有课程安排!')
            sleep(2)
        else:
            #driver.find_elements_by_class_name('XCUIElementTypeButton')[1].click()
            driver.find_element_by_android_uiautomator('new UiSelector().text("进入教室")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
            sleep(8)
            others=driver.find_elements_by_android_uiautomator('new UiSelector().text("确定")')
            if len(others)!=0:
                driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
                sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_002b_enteredClassroom_R.png'
            driver.save_screenshot(sf0)
            sleep(2)
            wait_sign=driver.find_elements_by_android_uiautomator('new UiSelector().text("请等待老师进入教室")')
            if len(wait_sign)!=0:
                print('\nThere is a sign:请等待老师进入教室')
                sleep(2)
            #呼叫老师
            driver.find_element_by_android_uiautomator('new UiSelector().text("呼叫老师")').click()
            sleep(5)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_002b_afterCallTeacher_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("退出")').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_002b_afterExitCR_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:等待老师进入（学生进入，老师未进入）----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('waitForTeacher'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_002_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)[等待老师进入（学生进入，老师未进入）]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
