#coding=utf-8
from appium import webdriver
import unittest,time,os,random
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

    def checkMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n004:查看乐谱----开始:'+now)
        login(self)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_004b_classMuisc_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        tt=driver.find_elements_by_accessibility_id('上节课程')
        if len(tt)!=0:
            driver.find_element_by_accessibility_id('上节课程').click()
            flag=driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
        else:
            flag=driver.find_elements_by_class_name('XCUIElementTypeStaticText')[2].text
        sleep(2)
        #ic upload1
        b=driver.find_elements_by_accessibility_id('查看乐谱')
        print('\n'+flag)
        print('\n已开始:'+str('已开始' in flag))
        print('\n已结束:'+str('已结束' in flag))
        sleep(2)
        if len(b)!=0:
            driver.find_element_by_accessibility_id('查看乐谱').click()
        else:
            driver.find_element_by_accessibility_id('上传乐谱').click()
        sleep(3)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_004b_muiscItems_R.png'
        driver.save_screenshot(sf)
        sleep(2)
        items=driver.find_elements_by_class_name('XCUIElementTypeCell')
        i=len(items)
        print('items:'+str(i))
        if i==1:
            print('本节课暂未上传乐谱')
            sleep(1)
        else:
            self=driver.find_elements_by_accessibility_id('自主上传乐谱')
            if len(self)!=0:
                driver.find_elements_by_accessibility_id('自主上传乐谱')[0].click()
                sleep(5)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='./'+now+'_004b_musicBySelfDetail_R.png'
                driver.save_screenshot(sf1)
                sleep(2)
                #turn page left/right and play music
                #turnpaage_play goes wrong here
                #turnpage_play(self)
                driver.swipe(600,600,-550,0,500)
                sleep(2)
                driver.swipe(50,600,550,0,500)
                sleep(2)
                driver.find_element_by_accessibility_id('编辑').click()
                sleep(2)
                driver.find_element_by_accessibility_id('ic drag').click()
                sleep(2)
                driver.find_element_by_accessibility_id('完成').click()
                sleep(2)
                if (not ('已开始' in flag)) and (not ('已结束' in flag)):
                    sleep(2)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='./'+now+'_004b_afterEdit_R.png'
                    driver.save_screenshot(sf2)
                    sleep(2)
                else:
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='./'+now+'_004b_editNotAllowed_R.png'
                    driver.save_screenshot(sf2)
                    sleep(2)
                    print('课程已开始／已结束后不允许编辑乐谱')
                    sleep(2)
                    driver.find_element_by_accessibility_id('ic nav back').click()
                    sleep(2)
            else:
                driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()
                sleep(10)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='./'+now+'_004b_classMusicDetail_R.png'
                driver.save_screenshot(sf2)
                sleep(2)
                #turn page left/right and play music
                #turnpaage_play goes wrong here
                #turnpage_play(self)
                driver.swipe(600,600,-550,0,500)
                sleep(2)
                driver.swipe(50,600,550,0,500)
                sleep(2)
                #Add play code here
                pb=driver.find_elements_by_accessibility_id('play')
                if len(pb)!=0:
                    driver.find_element_by_accessibility_id('play').click()
                    sleep(8)
                    driver.find_element_by_accessibility_id('play').click()
                    sleep(2)
                sleep(1)
                driver.find_element_by_accessibility_id('ic nav back').click()
                sleep(2)
            if (not ('已开始' in flag)) and (not ('已结束' in flag)):
                driver.find_element_by_accessibility_id('删除').click()
                sleep(2)
                driver.find_element_by_accessibility_id('确定').click()
                sleep(4)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf4='./'+now+'_004b_afterDelete_R.png'
                driver.save_screenshot(sf4)
                sleep(2)
            else:
                print('\n课程已开始／已结束后不允许删除乐谱')
                sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(2)
        driver.swipe(800,500,0,-220,500)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n004:查看乐谱----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('checkMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_004b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(查看乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
