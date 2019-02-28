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
        sleep(3)

    def uploadMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n005:上传乐谱----开始:'+now)
        login(self)
        sleep(4)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_class_name('XCUIElementTypeButton')
                bu[i+1].click()
                sleep(2)
                lis2=driver.find_elements_by_accessibility_id('查看乐谱')
                if len(lis2)!=0:
                    driver.find_element_by_accessibility_id('查看乐谱').click()
                    sleep(2)
                    break
        else:
            driver.find_element_by_accessibility_id('查看乐谱').click()
            sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(2)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(2)
        driver.find_element_by_accessibility_id('搜索书名或曲目名').click()
        sleep(2)
        edit=driver.find_element_by_class_name('XCUIElementTypeTextField')
        edit.set_value('车尔尼')
        sleep(1)
        #Toolbar Done Button
        #driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        #sleep(1)
        #driver.find_element_by_accessibility_id('Search').click()
        #确认
        TouchAction(self.driver).press(x=273,y=535).wait(100).release().perform()
        sleep(1)
        #搜索
        TouchAction(self.driver).press(x=273,y=535).wait(100).release().perform()
        sleep(3)
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(2)
        driver.find_element_by_accessibility_id('添加乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_005b_afterUploadedMusic_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        #first music
        driver.find_element_by_class_name('XCUIElementTypeCell').click()
        sleep(5)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_005b_uploadedMusicDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
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
    testunit.addTest(TestTeacher('uploadMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_005b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(上传乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
