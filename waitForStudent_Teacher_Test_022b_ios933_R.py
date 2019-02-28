#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
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
        sleep(3)

    def waitForStudent(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n022:等待学生进入（老师进入，学生未进入）----开始:'+now)
        login(self)
        sleep(3)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_class_name('XCUIElementTypeButton')
                bu[i+1].click()
                sleep(2)
                lis2=driver.find_elements_by_accessibility_id('历史课单')
                if len(lis2)!=0:
                    #历史课单 middle
                    driver.find_elements_by_accessibility_id('进入教室')[0].click()
                    sleep(5)
                    break
        else:
            #历史课单 top
            driver.swipe(500,400,0,-183,1000)
            sleep(2)
            driver.find_elements_by_accessibility_id('进入教室')[1].click()
            sleep(5)
        sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_022b_enteredClassroom_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('查看上课乐谱').click()
        sleep(3)
        o2=driver.find_elements_by_accessibility_id('好')
        if len(o2)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_022b_checkClassSheet_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('查看上课要求').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_022b_checkClassNote_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('ic cancel').click()
        sleep(3)
        """
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_022b_afterlongWait_R.png'
        driver.save_screenshot(sf3)
        sleep(2)
        """
        driver.find_element_by_accessibility_id('退出').click()
        sleep(2)
        driver.find_element_by_accessibility_id('其他原因退出').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n022:等待学生进入（老师进入，学生未进入）----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('waitForStudent'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_022b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机[等待学生进入(老师进入，学生未进入)]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
