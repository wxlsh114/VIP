#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher_ios933 import login,logout,turnpage_play

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


    def displayPlayMusic(self):
        driver=self.driver
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n028:乐谱库乐谱的显示播放----开始:'+now)
        login(self)
        sleep(4)
        driver.find_element_by_accessibility_id('乐谱库').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_028b_allMusic_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_028b_Music_P_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        driver.find_element_by_accessibility_id('小提琴').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_028b_Music_V_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('手风琴').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_028b_Music_hand_R.png'
        driver.get_screenshot_as_file(sf3)
        sleep(2)
        """
        driver.find_element_by_accessibility_id('古筝').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf4='./'+now+'_028b_Music_hand_old.png'
        driver.get_screenshot_as_file(sf4)
        sleep(2)
        """
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(3)
        driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
        sleep(2)
        #first music
        driver.find_element_by_class_name('XCUIElementTypeCell').click()
        sleep(3)
        turnpage_play(self)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_028b_uploadedMusicDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n028:乐谱库乐谱的显示播放----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('displayPlayMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_028b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(乐谱库乐谱的显示播放)测试报告by Appium',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
