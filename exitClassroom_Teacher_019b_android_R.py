#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
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

    def exitClassroom(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n019:退出教室----开始:'+now)
        login(self)
        sleep(3)
        lis1=driver.find_elements_by_android_uiautomator('new UiSelector().text("本日暂时没有课程安排")')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/courseCountTv')[i+1]
                if (bu.text!='0'):
                    bu.click()
                    sleep(2)
                    #历史课单 middle
                    #driver.swipe(1000,1600,1000,1100,1000)
                    #sleep(2)
                    btn=driver.find_elements_by_android_uiautomator('new UiSelector().text("进入教室")')[0]
                    btn.click()
                    sleep(5)
                    break
        else:
            driver.swipe(1000,1600,1000,1100,1000)
            sleep(2)
            btn=driver.find_elements_by_android_uiautomator('new UiSelector().text("进入教室")')[1]
            btn.click()
            sleep(5)
        allow=driver.find_elements_by_android_uiautomator('new UiSelector().text("始终允许")')
        if len(allow)!=0:
            driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
            sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_019b_cancel_exitClassroom_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("结束本次课程")').click()
        sleep(3)
        btn.click()
        sleep(5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("网络不好，退出重连")').click()
        sleep(3)
        btn.click()
        sleep(5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("其他原因退出")').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n019:退出教室----结束:'+now)
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('exitClassroom'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_019b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[退出教室]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
