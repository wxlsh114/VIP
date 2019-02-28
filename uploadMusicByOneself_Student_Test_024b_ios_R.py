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

    def uploadMusicByOneself(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:自主上传乐谱----开始:'+now)
        login(self)
        sleep(3)
        tt=driver.find_elements_by_accessibility_id('上节课程')
        if len(tt)!=0:
            driver.find_element_by_accessibility_id('上节课程').click()
            flag=driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        else:
            flag=driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        sleep(2)
        #ic upload1
        print('\n'+flag)
        print('\n已开始:'+str('已开始' in flag))
        print('\n已结束:'+str('已结束' in flag))
        sleep(1)
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
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_024b_uploadedMusicIni_R.png'
        driver.get_screenshot_as_file(sf)
        sleep(2)
        lis=driver.find_elements_by_class_name('XCUIElementTypeCell')
        i=len(lis)
        print('\ni:'+str(i)+'----实际已有乐谱数量:'+str(i-1))
        sleep(2)
        #delete existing music
        if (i!=1 and (not ('已开始' in flag) and not ('已结束' in flag))):
            for j in range(i-1):
                driver.find_element_by_accessibility_id('删除').click()
                sleep(3)
                driver.find_element_by_accessibility_id('确定').click()
                sleep(2)
            sleep(2)
            driver.find_element_by_accessibility_id('上传乐谱').click()
            sleep(2)
            """
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(2)
            driver.find_element_by_accessibility_id('取消').click()
            sleep(2)
            """
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(3)
            driver.find_element_by_accessibility_id('最近上过的乐谱').click()
            sleep(3)
            driver.find_element_by_accessibility_id('   添 加   ').click()
            #add=driver.find_elements_by_class_name('XCUIElementTypeButton')[1]
            #add.click()
            #print('S'+add.text+'S')
            sleep(3)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_024b_uploadedMusicByBefore_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            #[i] for not deleting firstly
            driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByBeforeDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            driver.find_element_by_accessibility_id('上传乐谱').click()
            sleep(3)
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(3)
            driver.find_element_by_accessibility_id('从相册选择').click()
            sleep(2)
            driver.find_elements_by_class_name('XCUIElementTypeButton')[7].click()
            sleep(2)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByAlbum_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            #[i+1] for not deleting firstly
            driver.find_elements_by_class_name('XCUIElementTypeCell')[2].click()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByAlbumDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            driver.find_element_by_accessibility_id('上传乐谱').click()
            sleep(2)
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(3)
            driver.find_element_by_accessibility_id('拍照上传').click()
            sleep(2)
            driver.find_element_by_accessibility_id('ic_ photograph').click()
            sleep(2)
            aler2=driver.find_elements_by_accessibility_id('好')
            if len(aler2)!=0:
                driver.find_element_by_accessibility_id('好').click()
                sleep(3)
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="FrontBackFacingCameraChooser"]').click()
            #TouchAction(self.driver).press(x=343,y=619).wait(100).release().perform()
            sleep(3)
            #PhotoCapture
            driver.find_element_by_accessibility_id('PhotoCapture').click()
            sleep(2)
            driver.find_element_by_accessibility_id('使用照片').click()
            sleep(3)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='./'+now+'_024b_uploadedMusicBySelfie_R.png'
            driver.get_screenshot_as_file(sf1)
            sleep(2)
            #[i+2] for not deleting firstly
            driver.find_elements_by_class_name('XCUIElementTypeCell')[3].click()
            sleep(8)
        else:
            driver.find_element_by_accessibility_id('上传乐谱').click()
            sleep(2)
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(2)
            driver.find_element_by_accessibility_id('取消').click()
            sleep(2)
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(3)
            driver.find_element_by_accessibility_id('最近上过的乐谱').click()
            sleep(3)
            driver.find_element_by_accessibility_id('   添 加   ').click()
            #add=driver.find_elements_by_class_name('XCUIElementTypeButton')[1]
            #add.click()
            #print('S'+add.text+'S')
            sleep(3)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_024b_uploadedMusicByBefore_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            #[i] for not deleting firstly
            driver.find_elements_by_class_name('XCUIElementTypeCell')[i].click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByBeforeDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            driver.find_element_by_accessibility_id('上传乐谱').click()
            sleep(3)
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(3)
            driver.find_element_by_accessibility_id('从相册选择').click()
            sleep(2)
            driver.find_elements_by_class_name('XCUIElementTypeButton')[4].click()
            sleep(2)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByAlbum_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            #[i+1] for not deleting firstly
            driver.find_elements_by_class_name('XCUIElementTypeCell')[i+1].click()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByAlbumDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
            driver.find_element_by_accessibility_id('上传乐谱').click()
            sleep(2)
            driver.find_element_by_accessibility_id('自主上传').click()
            sleep(3)
            driver.find_element_by_accessibility_id('拍照上传').click()
            sleep(2)
            driver.find_element_by_accessibility_id('ic_ photograph').click()
            sleep(2)
            aler1=driver.find_elements_by_accessibility_id('好')
            if len(aler1)!=0:
                driver.find_element_by_accessibility_id('好').click()
                sleep(3)
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="FrontBackFacingCameraChooser"]').click()
            #TouchAction(self.driver).press(x=343,y=619).wait(100).release().perform()
            sleep(3)
            #PhotoCapture
            driver.find_element_by_accessibility_id('PhotoCapture').click()
            sleep(2)
            driver.find_element_by_accessibility_id('使用照片').click()
            sleep(3)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='./'+now+'_024b_uploadedMusicBySelfie_R.png'
            driver.get_screenshot_as_file(sf1)
            sleep(2)
            #[i+2] for not deleting firstly
            driver.find_elements_by_class_name('XCUIElementTypeCell')[i+2].click()
            sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_024b_uploadedMusicBySelfieDetail_R.png'
        driver.get_screenshot_as_file(sf2)
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:自主上传乐谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('uploadMusicByOneself'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_024b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(自主上传乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
