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
        sleep(2)

    def checkClassMusic(self):
        driver=self.driver
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n029:课程准备查看乐谱----开始:'+now)
        login(self)
        sleep(4)
        flag=driver.find_elements_by_accessibility_id('课程已结束')
        if len(flag)!=0:
            print('\n课程已结束: True')
        else:
            print('\n课程已结束: False')
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
            # 查看乐谱top
            driver.find_element_by_accessibility_id('查看乐谱').click()
            sleep(2)
        sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_029b_classMuisc_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        
        items=driver.find_elements_by_class_name('XCUIElementTypeCell')
        i=len(items)
        print('\nitems:'+str(i))
        if i==0:
            print('本节课暂未上传乐谱')
            sleep(1)
        else:
            self=driver.find_elements_by_accessibility_id('自主上传')
            if len(self)!=0:
                driver.find_element_by_accessibility_id('自主上传').click()
                sleep(5)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='./'+now+'_029b_musicBySelfDetail_R.png'
                driver.save_screenshot(sf1)
                sleep(2)
                #turn page left/right
                list=driver.find_elements_by_accessibility_id('ic next1')
                if len(list)!=0:
                    driver.find_elements_by_accessibility_id('ic next1')[0].click()
                    sleep(1)
                    driver.find_elements_by_accessibility_id('ic previous')[0].click()
                    sleep(1)
                driver.find_element_by_accessibility_id('编辑').click()
                sleep(2)
                #xyz
                driver.find_element_by_accessibility_id('ic drag').click()
                sleep(2)
                driver.find_element_by_accessibility_id('完成').click()
                sleep(4)
                if len(flag)==0:
                    sleep(2)
                else:                   
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='./'+now+'_029b_editNotAllowed_R.png'
                    driver.save_screenshot(sf2)
                    sleep(2)
                    print('课程结束后不允许编辑乐谱')
                    sleep(1)
                    driver.find_element_by_accessibility_id('返回').click()
                    sleep(2)
            else:
                driver.find_element_by_class_name('XCUIElementTypeCell').click()
                sleep(10)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='./'+now+'_029b_classMusicDetail_R.png'
                driver.save_screenshot(sf2)
                sleep(2)
                #turnpage_play(self)
                list=driver.find_elements_by_accessibility_id('ic next1')
                if len(list)!=0:
                    driver.find_elements_by_accessibility_id('ic next1')[0].click()
                    sleep(1)
                    driver.find_elements_by_accessibility_id('ic previous')[0].click()
                    sleep(1)
                #Add play code here
                p=driver.find_elements_by_accessibility_id('ic play2')
                if len(p)!=0:
                    driver.find_element_by_accessibility_id('ic play2').click()
                    sleep(8)
                    driver.find_element_by_accessibility_id('ic play2').click()
                    sleep(2)
                #ic nav back
                driver.find_element_by_accessibility_id('ic nav back').click()
                sleep(2)
            driver.find_element_by_accessibility_id('删除').click()
            sleep(2)
            #删除
            driver.find_element_by_accessibility_id('确定').click()
            sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(3)
        driver.swipe(500,400,0,-250,1000)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(2)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n029:课程准备查看乐谱----结束:'+now)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('checkClassMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_029b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(课程准备查看乐谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
