#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
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

    def callService(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n023:联系客服----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.find_element_by_accessibility_id('呼叫客服').click()
        sleep(2)
        driver.find_element_by_accessibility_id('呼叫').click()
        sleep(2)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        """
        aler=driver.find_elements_by_accessibility_id('好')
        if len(aler)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
        """
        driver.swipe(800,500,0,-220,500)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n023:联系客服----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('callService'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_023b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(联系客服)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
