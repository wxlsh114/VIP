#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher import login,logout,turnpage_play


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

    def displayPlayMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n028:乐谱库乐谱的显示播放----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("乐谱库")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_028b_allMusic_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("钢琴")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_028b_Music_P_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("小提琴")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_028b_Music_V_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("手风琴")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_028b_Music_hand_R.png'
        driver.get_screenshot_as_file(sf3)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("古筝")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf4='./'+now+'_028b_Music_hand_old.png'
        driver.get_screenshot_as_file(sf4)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("钢琴")').click()
        sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/tvMusicBookName').click()
        sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/lookMusicScoreLl').click()
        sleep(3)
        turnpage_play(self)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_028b_musicDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("乐谱库")').click()
        sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/leftTv').click()
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n028:乐谱库乐谱的显示播放----结束:'+now)
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('displayPlayMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_028b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[乐谱库乐谱的显示播放]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
