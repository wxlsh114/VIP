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
        sleep(3)


    def changePwd(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n025:修改密码----开始:'+now)
        login(self)
        sleep(3)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.find_element_by_accessibility_id('修改密码').click()
        sleep(2)
        old=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
        old.click()
        old.set_value('123456')
        sleep(1)
        new1=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
        new1.click()
        new1.set_value('123456wxl')
        sleep(1)
        new2=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[2]
        new2.click()
        new2.set_value('123456wxl')
        #driver.find_element_by_accessibility_id('完成').click()
        TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
        sleep(1)
        driver.find_element_by_accessibility_id('确认').click()
        sleep(3)
        driver.swipe(500,500,0,-250,1000)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        #check new password
        mo=driver.find_element_by_class_name('XCUIElementTypeTextField')
        mo.click()
        mo.set_value('18311111111')
        #driver.find_element_by_accessibility_id('完成').click()
        TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
        sleep(1)
        pwd=driver.find_element_by_class_name('XCUIElementTypeSecureTextField')
        pwd.click()
        pwd.set_value('123456wxl')
        #完成
        TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
        sleep(2)
        #登 录
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="登录"]').click()
        #TouchAction(self.driver).press(x=187,y=480).wait(100).release().perform()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_025b_reLogin_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n025:修改密码----结束:'+now)
    
    def changePwdBack(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n025:修改密码回原值----开始:'+now)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
        #跳 过
        driver.find_elements_by_accessibility_id('跳 过')[1].click()
        sleep(1)
        mo=driver.find_element_by_class_name('XCUIElementTypeTextField')
        mo.click()
        mo.set_value('18311111111')
        #driver.find_element_by_accessibility_id('完成').click()
        TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
        sleep(1)
        pwd=driver.find_element_by_class_name('XCUIElementTypeSecureTextField')
        pwd.click()
        pwd.set_value('123456wxl')
        #driver.find_element_by_accessibility_id('完成').click()
        TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
        sleep(1)
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="登录"]').click()
        sleep(3)
        #someone already logged in
        another=driver.find_elements_by_accessibility_id('确定')
        if len(another)!=0:
            driver.find_element_by_accessibility_id('确定').click()
            sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
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
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.find_element_by_accessibility_id('修改密码').click()
        sleep(2)
        old=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
        old.click()
        old.set_value('123456wxl')
        sleep(1)
        new1=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
        new1.click()
        new1.set_value('123456')
        sleep(1)
        new2=driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[2]
        new2.click()
        new2.set_value('123456')
        #driver.find_element_by_accessibility_id('完成').click()
        TouchAction(self.driver).press(x=290,y=330).wait(100).release().perform()
        sleep(1)
        driver.find_element_by_accessibility_id('确认').click()
        sleep(3)
        driver.swipe(500,500,0,-250,1000)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n025:修改密码回原值----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('changePwd'))
    testunit.addTest(TestTeacher('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_025b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(修改密码/重置密码)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
