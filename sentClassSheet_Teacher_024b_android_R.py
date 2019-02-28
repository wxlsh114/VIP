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

    def sentClassSheet(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:已发送陪练单----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("陪练单")').click()
        sleep(2)
        another=driver.find_elements_by_android_uiautomator('new UiSelector().text("好")')
        if len(another)!=0:
            driver.find_element_by_android_uiautomator('new UiSelector().text("好")').click()
            sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("已发送陪练单")').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_024b_sentClassSheet_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("查看课单")').click()
        sleep(10)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_024b_sentClassSheetDetailTop_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        driver.swipe(1000,1600,1000,100,1000)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_024b_sentClassSheetDetailTail_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        p=driver.find_elements_by_xpath('//android.view.View[contains(@content-desc,"点击播放语音评价")]')
        print(str(len(p)))
        if len(p)!=0:
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"点击播放语音评价")]').click()
            sleep(8)
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"点击播放语音评价")]').click()
            sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/leftTv').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:已发送陪练单----结束:'+now)
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('sentClassSheet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_024b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[查看已发送陪练单]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
