#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from appium.webdriver.common.touch_action import TouchAction
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

    def aboutUs(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n010:关于我们----开始:'+now)
        login(self)
        sleep(3)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.swipe(800,500,0,-450,500)
        sleep(2)
        driver.find_element_by_accessibility_id('关于我们').click()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_010b_aboutUsTop_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.swipe(800,600,0,-500,500)
        sleep(2)
        driver.swipe(800,600,0,-500,500)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_010b_aboutUsMiddle_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.swipe(800,600,0,-500,500)
        sleep(2)
        driver.swipe(800,600,0,-500,500)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_010b_aboutUsTail_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.swipe(800,500,0,-450,500)
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n010:关于我们----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('aboutUs'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_010b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(关于我们)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
