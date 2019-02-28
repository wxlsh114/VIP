#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher import login,logout

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestTeacher(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'PRA-AL00'
        #desired_caps['udid'] = 'HMKNW17225011700'
        desired_caps['app'] = PATH('../VIPTeacher_2.0.3.apk')
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass_teacher.test'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()
        

    def aboutUs(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n010:关于我们----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(2)
        driver.swipe(1000,1600,1000,1250,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("关于我们")').click()
        sleep(10)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_010b_aboutUsTop_R.png'
        driver.save_screenshot(sf3)
        sleep(2)
        driver.swipe(1000,1700,1000,100,1000)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_010b_aboutUsMiddle_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.swipe(1000,1700,1000,100,1000)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_010b_aboutUsTail_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/leftTv').click()
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n010:关于我们----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('aboutUs'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_010b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[关于我们]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
