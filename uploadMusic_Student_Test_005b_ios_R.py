#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout,turnpage_play

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

    def uploadMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n005:上传乐谱----开始:'+now)
        login(self)
        sleep(2)
        #ic upload1
        b=driver.find_elements_by_accessibility_id('上传乐谱')
        if len(b)!=0:
            driver.find_element_by_accessibility_id('上传乐谱').click()
        else:
            #ic Sheet music
            driver.find_element_by_accessibility_id('查看乐谱').click()
        sleep(2)
        aler=driver.find_elements_by_accessibility_id('好')
        if len(aler)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_005b_beforeAddMusic_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(2)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(2)
        driver.find_element_by_accessibility_id('小提琴').click()
        sleep(2)
        driver.find_element_by_accessibility_id('手风琴').click()
        sleep(2)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(2)
        driver.find_element_by_accessibility_id('搜索书名或者曲目名').click()
        sleep(2)
        driver.find_element_by_accessibility_id('车尔尼').click()
        sleep(2)
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(2)
        #first music
        driver.find_element_by_class_name('XCUIElementTypeCell').click()
        sleep(3)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('   添 加   ').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_005b_afterAddMusic_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n005:上传乐谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('uploadMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_005b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(上传乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
