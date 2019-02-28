#coding=utf-8
from appium import webdriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from appium.webdriver.common.touch_action import TouchAction
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
        
    def searchMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n003:搜索添加乐谱库乐谱----开始:'+now)
        login(self)
        sleep(3)
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
            sleep(3)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(2)
        #hot search
        driver.find_element_by_accessibility_id('搜索书名或者曲目名').click()
        sleep(3)
        driver.find_element_by_accessibility_id('考级').click()
        sleep(3)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(3)
        driver.find_element_by_accessibility_id('小提琴').click()
        sleep(3)
        driver.find_element_by_accessibility_id('手风琴').click()
        sleep(3)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(3)
        #first music
        driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
        sleep(3)
        #first item
        driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_003b_searchedMusicByHotDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        """
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        driver.find_element_by_accessibility_id('全部').click()
        sleep(2)
        """
        #whole music name
        s=driver.find_element_by_class_name('XCUIElementTypeTextField')
        s.click()
        s.set_value('车尔尼299 No.02')
        sleep(1)
        driver.find_element_by_accessibility_id('Search').click()
        sleep(4)
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(3)
        driver.find_element_by_class_name('XCUIElementTypeCell').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_003b_searchedMusicByWholenameDetail_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        driver.find_element_by_accessibility_id('全部').click()
        sleep(2)
        #keyword
        s=driver.find_element_by_class_name('XCUIElementTypeTextField')
        s.click()
        s.set_value('299 No.07')
        sleep(1)
        driver.find_element_by_accessibility_id('Search').click()
        sleep(4)
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(3)
        driver.find_element_by_class_name('XCUIElementTypeCell').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_003b_searchedMusicByKeywordDetail_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n003:搜索添加乐谱库乐谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('searchMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_003b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(搜索添加乐谱库乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
