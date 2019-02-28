#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestStudent(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'PRA-AL00'
        #desired_caps['udid'] = 'HMKNW17225011700'
        desired_caps['app'] = PATH('../VIPStudent_2.0.4.apk')
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass.pnlclass_student.ceshi'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()
        
    def changePwd(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:修改密码----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("修改密码")').click()
        sleep(2)
        old=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etOldPass')
        old.click()
        old.set_value('123456')
        sleep(1)
        new=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etNewPass')
        new.click()
        new.set_value('123456wxl')
        sleep(1)
        #com.android.gallery3d:id/head_select_right
        again=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etConfirmNewPass')
        again.click()
        again.set_value('123456wxl')
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确认")').click()
        sleep(3)
        driver.swipe(1000,1600,1000,1250,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        sleep(2)
        user=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etUserName')
        user.click()
        user.set_value('13923121234')
        sleep(1)
        pwd=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etPassword')
        pwd.click()
        pwd.set_value('123456wxl')
        sleep(1)
        driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnLogin').click()
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_021b_relogin_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(3)
        driver.swipe(1000,1600,1000,1250,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:修改密码----结束:'+now)

    def changePwdBack(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:重置密码----开始:'+now)
        driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
        sleep(2)
        user=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etUserName')
        user.click()
        user.set_value('13923121234')
        sleep(1)
        pwd=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etPassword')
        pwd.click()
        pwd.set_value('123456wxl')
        sleep(1)
        driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnLogin').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
        sleep(2)
        #test now
        driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
        sleep(4)
        driver.find_element_by_android_uiautomator('new UiSelector().text("停止录音")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("有听到声音")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("您已完成测试")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("修改密码")').click()
        sleep(2)
        old=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etOldPass')
        old.click()
        old.set_value('123456wxl')
        sleep(1)
        new=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etNewPass')
        new.click()
        new.set_value('123456')
        sleep(1)
        #com.android.gallery3d:id/head_select_right
        again=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etConfirmNewPass')
        again.click()
        again.set_value('123456')
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确认")').click()
        sleep(3)
        driver.swipe(1000,1600,1000,1250,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:重置密码----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    #testunit.addTest(TestStudent('changePwd'))
    testunit.addTest(TestStudent('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_021b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)[修改密码／重置密码]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
