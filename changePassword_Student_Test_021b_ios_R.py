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

    def changePwd(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:修改密码----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.find_element_by_accessibility_id('修改密码').click()
        sleep(2)
        old=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
        old.click()
        old.set_value('123456')
        sleep(2)
        new1=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
        new1.click()
        new1.set_value('123456wxl')
        sleep(2)
        new2=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[2]
        new2.click()
        new2.set_value('123456wxl')
        sleep(2)
        driver.find_element_by_accessibility_id('确认').click()
        sleep(3)
        driver.swipe(800,500,0,-220,1000)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        driver.find_element_by_accessibility_id('登录').click()
        sleep(1)
        #check new password
        mo=driver.find_element_by_class_name('XCUIElementTypeTextField')
        mo.click()
        mo.clear()
        mo.set_value('14100000011')
        #driver.find_element_by_accessibility_id('完成').click()
        sleep(2)
        pwd=driver.find_element_by_class_name('XCUIElementTypeSecureTextField')
        pwd.click()
        pwd.set_value('123456wxl')
        sleep(2)
        #登 录
        #driver.find_element_by_accessibility_id('登 录').click()
        driver.find_elements_by_class_name('XCUIElementTypeButton')[2].click()
        #TouchAction(self.driver).press(x=187,y=416).wait(100).release().perform()
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_021b_reLogin_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        logout(self)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:修改密码----结束:'+now)
    
    def changePwdBack(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:重置密码----开始:'+now)
        sleep(2)
        driver.find_element_by_accessibility_id('允许').click()
        sleep(1)
        driver.find_element_by_accessibility_id('登录').click()
        sleep(1)
        mo=driver.find_element_by_class_name('XCUIElementTypeTextField')
        mo.click()
        mo.set_value('14100000011')
        sleep(1)
        pwd=driver.find_element_by_class_name('XCUIElementTypeSecureTextField')
        pwd.click()
        pwd.set_value('123456wxl')
        sleep(1)
        driver.find_elements_by_class_name('XCUIElementTypeButton')[2].click()
        #driver.find_element_by_accessibility_id('登录').click()
        sleep(3)
        #someone already logged in
        another=driver.find_elements_by_accessibility_id('确定')
        if len(another)!=0:
            driver.find_element_by_accessibility_id('确定').click()
            sleep(3)
        aler=driver.find_elements_by_accessibility_id('好')
        if len(aler)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        #test now
        driver.find_element_by_accessibility_id('开始测试').click()
        sleep(3)
        driver.find_element_by_accessibility_id('点击开始录音').click()
        sleep(3)
        driver.find_element_by_accessibility_id('停止录音').click()
        sleep(2)
        driver.find_element_by_accessibility_id('有听到声音').click()
        sleep(2)
        driver.find_element_by_accessibility_id('下一步').click()
        sleep(2)
        driver.find_element_by_accessibility_id('下一步').click()
        sleep(2)
        driver.find_element_by_accessibility_id('完成测试').click()
        sleep(2)
        #Got it.
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="ic guide btn"]').click()
        sleep(2)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.find_element_by_accessibility_id('修改密码').click()
        sleep(2)
        old=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
        old.click()
        old.set_value('123456wxl')
        sleep(2)
        new1=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
        new1.click()
        new1.set_value('123456')
        sleep(2)
        new2=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[2]
        new2.click()
        new2.set_value('123456')
        sleep(2)
        driver.find_element_by_accessibility_id('确认').click()
        sleep(4)
        driver.swipe(800,500,0,-220,500)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:重置密码----结束:'+now)
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('changePwd'))
    testunit.addTest(TestStudent('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_021b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(修改密码／重置密码)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
