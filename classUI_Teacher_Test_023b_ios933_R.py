#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher_ios933 import login,logout

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

    def classUI(self):
        driver=self.driver
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n023:登录成功后的课表界面----开始:'+now)
        login(self)
        sleep(4)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            print('今天没有课程!')
            sleep(2)
        else:
            #first class today
            driver.swipe(500,400,0,-182,1000)
            sleep(2)
            t=driver.find_elements_by_accessibility_id('进入教室')[1]
            if t.is_enabled():
                print('现在进入教室的按钮是红色的!')
                sleep(2)
            else:
                print('现在进入教室的按钮是灰色的!')
                sleep(2)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_023b_classUI_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n023:登录成功后的课表界面----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('classUI'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_023b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(登录成功后的课表界面)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
