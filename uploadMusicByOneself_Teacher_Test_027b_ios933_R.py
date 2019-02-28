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

    def uploadMusicByOneself(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n027:自主上传乐谱----开始:'+now)
        login(self)
        sleep(2)
        flag=driver.find_elements_by_accessibility_id('课程已结束')
        if len(flag)!=0:
            print('\n课程已结束:True')
        else:
            print('\n课程已结束:False')
        sleep(3)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_class_name('XCUIElementTypeButton')
                bu[i+1].click()
                sleep(2)
                lis2=driver.find_elements_by_accessibility_id('查看乐谱')
                if len(lis2)!=0:
                    #查看乐谱 middle
                    driver.find_element_by_accessibility_id('查看乐谱').click()
                    sleep(2)
                    break
        else:
            #查看乐谱 top
            driver.find_element_by_accessibility_id('查看乐谱').click()
            sleep(2)
        sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_027b_uploadedMusicItems_R.png'
        driver.get_screenshot_as_file(sf)
        sleep(2)
        items=driver.find_elements_by_class_name('XCUIElementTypeCell')
        i=len(items)
        print(str(i))
        sleep(2)
        if (i!=0 and len(flag)==0):
            for j in range(i):
                driver.find_element_by_accessibility_id('删除').click()
                sleep(2)
                driver.find_element_by_accessibility_id('确定').click()
                sleep(2)
            i=0
        sleep(3)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(3)
        """
        driver.find_element_by_accessibility_id('自主上传').click()
        sleep(3)
        driver.find_element_by_accessibility_id('取消').click()
        sleep(2)
        """
        driver.find_element_by_accessibility_id('自主上传').click()
        sleep(3)
        driver.find_element_by_accessibility_id('最近上过的乐谱').click()
        sleep(3)
        add=driver.find_elements_by_accessibility_id('添加')
        if len(add)!=0:
            driver.find_element_by_accessibility_id('添加').click()
            sleep(3)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_027b_uploadedMusicBybefore_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
            sleep(6)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_027b_uploadedMusicByAlbeforeDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            k=1
        else:
            k=0
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('自主上传').click()
        sleep(3)
        driver.find_element_by_accessibility_id('从相册选择').click()
        sleep(3)
        driver.find_elements_by_class_name('XCUIElementTypeButton')[8].click()
        sleep(3)
        driver.find_element_by_accessibility_id('完成').click()
        sleep(8)
        driver.find_element_by_accessibility_id('返回').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_027b_uploadedMusicByAlbum_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_elements_by_class_name('XCUIElementTypeCell')[i+k].click()
        sleep(6)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_027b_uploadedMusicByAlbumDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(3)
        driver.find_element_by_accessibility_id('自主上传').click()
        sleep(3)
        driver.find_element_by_accessibility_id('拍照上传').click()
        sleep(3)
        driver.find_element_by_accessibility_id('ic_camera').click()
        sleep(3)
        o3=driver.find_elements_by_accessibility_id('好')
        if len(o3)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
        driver.find_element_by_accessibility_id('FrontBackFacingCameraChooser').click()
        #TouchAction(self.driver).press(x=300,y=20).wait(100).release().perform()
        sleep(3)
        #PhotoCapture
        driver.find_element_by_accessibility_id('PhotoCapture').click()
        sleep(3)
        driver.find_element_by_accessibility_id('使用照片').click()
        sleep(3)
        driver.find_element_by_accessibility_id('完成').click()
        sleep(8)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_027b_uploadedMusicBySelfie_R.png'
        driver.get_screenshot_as_file(sf1)
        sleep(2)
        driver.find_elements_by_class_name('XCUIElementTypeCell')[i+k+1].click()
        sleep(6)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_027b_uploadedMusicBySelfieDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n027:自主上传乐谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('uploadMusicByOneself'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_027b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(自主上传乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
