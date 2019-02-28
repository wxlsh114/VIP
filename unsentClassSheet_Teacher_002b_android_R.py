#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
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

    def edit_send_Classshet(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:未发送课单----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("你有未发送课单")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_002_before_classsheet_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("编辑陪练单")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("上课表现")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("很好")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("音符准确度")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("一般")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("节奏准确度")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("尚可")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("连贯性")').click()
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("较好")').click()
        sleep(1)
        pyqk=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/noteEt')
        pyqk.click()
        pyqk.set_value('1234567890 abcdef')
        sleep(1)
        driver.swipe(1000,1000,1000,600,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
        sleep(8)
        driver.find_element_by_android_uiautomator('new UiSelector().text("点击停止计时")').click()
        sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/tapeNewTv').click()
        sleep(8)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/tapeNewTv').click()
        sleep(2)
        driver.swipe(1000,1000,1000,100,1000)                                           
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("存为草稿")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("存为草稿")').click()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_002b_afterSave_classsheet_R.png'
        driver.save_screenshot(sf3)
        sleep(2)
        """
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/leftTv').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("去查看")').click()
        sleep(2)
        """
        driver.find_element_by_android_uiautomator('new UiSelector().text("编辑陪练单")').click()
        sleep(2)
        driver.swipe(1000,1600,1000,100,1000)                                            
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("发送陪练单")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("发送")').click()
        sleep(5)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_002b_afterSent_classsheet_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/leftTv').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("陪练单")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("已发送陪练单")').click()
        sleep(2)
        #driver.swipe(1000,1600,1000,800,1000)
        #sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_002b_sent_classsheet_R.png'
        driver.save_screenshot(sf2)
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:未发送课单----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('edit_send_Classshet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_002_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[编辑未发送课单后发送]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
