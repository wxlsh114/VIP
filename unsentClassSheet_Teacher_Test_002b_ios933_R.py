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
        sleep(5)

    def edit_send_Classshet(self):
        driver=self.driver
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:未发送课单:编辑后保存再发送课单----开始:'+now)
        login(self)
        sleep(2)
        #driver.find_element_by_accessibility_id('去看看').click()
        #//XCUIElementTypeStaticText[@name="去看看"]
        TouchAction(self.driver).press(x=252,y=477).wait(100).release().perform()
        sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_002b_beforeSend_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('编辑陪练单').click()
        sleep(2)
        driver.find_element_by_accessibility_id('上课表现').click()
        sleep(1)
        TouchAction(self.driver).press(x=100,y=340).wait(100).release().perform()
        #driver.find_element_by_accessibility_id('很好').click()
        sleep(1)
        driver.find_element_by_accessibility_id('音符准确度').click()
        sleep(1)
        TouchAction(self.driver).press(x=228,y=307).wait(100).release().perform()
        #driver.find_element_by_accessibility_id('较好').click()
        sleep(1)
        driver.find_element_by_accessibility_id('节奏准确度').click()
        sleep(1)
        TouchAction(self.driver).press(x=92,y=370).wait(100).release().perform()
        #driver.find_element_by_accessibility_id('尚好').click()
        sleep(1)
        driver.find_element_by_accessibility_id('连贯性').click()
        sleep(1)
        TouchAction(self.driver).press(x=228,y=390).wait(100).release().perform()
        #driver.find_element_by_accessibility_id('一般').click()
        sleep(1)
        #'请填写本节课的陪练曲目，下节课的备注。'
        edit=driver.find_elements_by_class_name('XCUIElementTypeTextView')[0]
        #sleep(2)
        edit.click()
        edit.set_value('123456789陪练曲目114')
        #driver.find_element_by_accessibility_id('完成').click()
        TouchAction(self.driver).press(x=290,y=294).wait(100).release().perform()
        sleep(2)
        pb=driver.find_elements_by_accessibility_id('ic play2')
        if len(pb)==0:
            driver.find_element_by_accessibility_id('ACPractice recode can').click()
            sleep(8)
            driver.find_element_by_accessibility_id('ic time out').click()
            sleep(2)
        driver.find_element_by_accessibility_id('ic play2').click()
        sleep(6)
        driver.find_element_by_accessibility_id('ic time out').click()
        sleep(2)
        driver.swipe(500,500,0,-450,1000)
        sleep(1)
        driver.swipe(500,500,0,-450,1000)
        sleep(1)
        driver.find_element_by_accessibility_id('存为草稿').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(5)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_002b_afterSave_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(1)
        driver.find_element_by_accessibility_id('编辑陪练单').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_002b_classSheet1_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.swipe(500,500,0,-450,1000)
        sleep(1)
        driver.swipe(500,500,0,-450,1000)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_002b_classSheet2_R.png'
        driver.get_screenshot_as_file(sf3)
        sleep(2)
        driver.find_element_by_accessibility_id('提交陪练单').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(5)
        driver.find_element_by_accessibility_id('已发送陪练单').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf4='./'+now+'_002b_sentClassSheet_R.png'
        driver.get_screenshot_as_file(sf4)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:未发送课单:编辑后保存再发送课单----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('edit_send_Classshet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_002b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(编辑未发送课单后发送课单)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
