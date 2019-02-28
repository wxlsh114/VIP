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
        
    def searchAddMusicClassroom(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n033:进入教室搜索添加乐谱----开始:'+now)
        login(self)
        sleep(4)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_class_name('XCUIElementTypeButton')
                bu[i+1].click()
                sleep(2)
                lis2=driver.find_elements_by_accessibility_id('历史课单')
                if len(lis2)!=0:
                    driver.find_elements_by_accessibility_id('进入教室')[0].click()
                    sleep(5)
                    break
        else:
            driver.swipe(500,400,0,-183,1000)
            sleep(2)
            driver.find_elements_by_accessibility_id('进入教室')[1].click()
            sleep(5)
        sleep(3)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
        sleep(3)
        driver.find_element_by_accessibility_id('查看上课乐谱').click()
        sleep(3)
        o2=driver.find_elements_by_accessibility_id('好')
        if len(o2)!=0:
            driver.find_element_by_accessibility_id('好').click()
        sleep(3)
        items=driver.find_elements_by_class_name('XCUIElementTypeCell')
        i=len(items)
        print(str(i))
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_033b_beforeAddedMusic_R.png'
        driver.get_screenshot_as_file(sf3)
        sleep(2)
        if i!=0:
            for j in range(i):
                driver.find_element_by_accessibility_id('删除').click()
                sleep(2)
                driver.find_element_by_accessibility_id('确定').click()
                sleep(2)
        sleep(2)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('小提琴').click()
        sleep(3)
        driver.find_element_by_accessibility_id('手风琴').click()
        sleep(3)
        #driver.find_element_by_accessibility_id('古筝').click()
        #sleep(2)
        driver.find_element_by_accessibility_id('钢琴').click()
        sleep(3)
        #hot search
        driver.find_element_by_accessibility_id('搜索书名或曲目名').click()
        sleep(3)
        driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="车尔尼"])[3]').click()
        sleep(3)
        #first music
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(3)
        driver.find_element_by_accessibility_id('车尔尼299 No.03').click()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_033b_searchedMusicByHotDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('返回').click()
        sleep(3)
        driver.find_element_by_accessibility_id('添加乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(3)
        driver.find_element_by_accessibility_id('全部').click()
        sleep(3)
        #whole music name
        driver.find_element_by_accessibility_id('搜索书名或曲目名').click()
        sleep(2)
        s=driver.find_element_by_class_name('XCUIElementTypeTextField')
        s.click()
        s.set_value('车尔尼299 No.02')
        sleep(1)
        #driver.find_element_by_accessibility_id('Search').click()
        #确认
        TouchAction(self.driver).press(x=273,y=535).wait(100).release().perform()
        sleep(1)
        #搜索
        TouchAction(self.driver).press(x=273,y=535).wait(100).release().perform()
        sleep(4)
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(3)
        driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_033b_searchedMusicByWholenameDetail_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('返回').click()
        sleep(2)
        t1=driver.find_elements_by_accessibility_id('添加乐谱')
        if len(t1)!=0:
            driver.find_element_by_accessibility_id('添加乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        driver.find_element_by_accessibility_id('全部').click()
        sleep(2)
        #keyword
        driver.find_element_by_accessibility_id('搜索书名或曲目名').click()
        sleep(2)
        s=driver.find_element_by_class_name('XCUIElementTypeTextField')
        s.click()
        s.set_value('299 No.05')
        sleep(1)
        #driver.find_element_by_accessibility_id('Search').click()
        #确认
        TouchAction(self.driver).press(x=273,y=535).wait(100).release().perform()
        sleep(1)
        #搜索
        TouchAction(self.driver).press(x=273,y=535).wait(100).release().perform()
        sleep(4)
        driver.find_element_by_accessibility_id('包含该曲目').click()
        sleep(3)
        #driver.find_elements_by_accessibility_id('车尔尼299 No.05')[1].click()
        driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_033b_searchedMusicByKeywordDetail_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        driver.find_element_by_accessibility_id('返回').click()
        sleep(3)
        t2=driver.find_elements_by_accessibility_id('添加乐谱')
        if len(t2)!=0:
            driver.find_element_by_accessibility_id('添加乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_033b_afterAddedMusic_R.png'
        driver.get_screenshot_as_file(sf)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('退出').click()
        sleep(3)
        driver.find_element_by_accessibility_id('其他原因退出').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n033:进入教室搜索添加乐谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('searchAddMusicClassroom'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_033b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(进入教室搜索添加乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
