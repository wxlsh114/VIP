#coding=utf-8
import unittest,time,os,random
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
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

    def checkClassSheet(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n022:查看陪练单并评价老师----开始:'+now)
        login(self)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("陪练单")').click()
        sleep(3)
        i=random.randrange(0,3,1)
        driver.find_elements_by_android_uiautomator('new UiSelector().text("查看陪练单")')[i].click()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_022b_classSheetDetail1_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.swipe(1000,1600,1000,100,1000)
        sleep(2)
        driver.swipe(1000,1600,1000,100,1000)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_022b_classSheetDetail2_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        #点击播放语音评价
        current=driver.current_context
        print(current)
        print(driver.contexts)
        #print(driver.page_source)
        sleep(2)
        #context_name='WEBVIEW_com.android.browser'
        #driver.switch_to.context('WEBVIEW_com.android.browser')
        #sleep(5)
        p=driver.find_elements_by_xpath('//android.view.View[contains(@content-desc,"点击播放语音评价")]')
        print(str(len(p)))
        sleep(2)
        """
        context_name='WEBVIEW_com.android.browser'
        driver.switch_to.context(context_name)
        sleep(1)
        """
        #点击播放语音评价
        if len(p)!=0:
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"点击播放语音评价")]').click()
            sleep(4)
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"点击播放语音评价")]').click()
            sleep(3)
        judge=driver.find_elements_by_xpath('//android.widget.Button[contains(@content-desc,"评价老师")]')
        print(str(len(judge)))
        if len(judge)!=0:
            driver.find_element_by_xpath('//android.widget.Button[contains(@content-desc,"评价老师")]').click()
            sleep(5)
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"满意")]').click()
            sleep(2)
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"非常耐心")]').click()
            sleep(2)
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"声音甜美")]').click()
            sleep(2)
            driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"互动性强")]').click()
            sleep(2)
            driver.swipe(1000,1600,1000,800,1000)
            sleep(2)
            #student_comment ?
            #所有评价都将匿名并延迟告知老师
            edit=driver.find_element_by_android_uiautomator('new UiSelector().text("所有评价都将匿名并延迟告知老师")')
            edit.click()
            edit.set_value('No Chinese characters so far/123456 abcdefg')
            sleep(1)
            driver.find_element_by_xpath('//android.widget.Button[contains(@content-desc,"提交评价")]').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n022:查看陪练单并评价老师----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('checkClassSheet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_022b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)[查看陪练单并评价老师]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
