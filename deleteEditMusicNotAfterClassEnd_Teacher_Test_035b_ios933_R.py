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


    def deleteEditMusicNotEnd(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n035:非课程结束后删除/编辑曲谱----开始:'+now)
        login(self)
        sleep(4)
        flag=driver.find_elements_by_accessibility_id('课程已结束')
        if len(flag)!=0:
            print('\n课程已结束:True')
        else:
            print('\n课程已结束:False')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_035b_classUI_R.png'
        driver.save_screenshot(sf)
        sleep(2)
        lis1=driver.find_elements_by_accessibility_id('本日暂时没有课程安排')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_class_name('XCUIElementTypeButton')
                bu[i+1].click()
                sleep(2)
                lis2=driver.find_elements_by_accessibility_id('历史课单')
                if len(lis2)!=0:
                    #查看乐谱 middle
                    #driver.find_elements_by_class_name('XCUIElementTypeButton')[8].click()
                    driver.find_element_by_accessibility_id('查看乐谱').click()
                    sleep(2)
                    break
        else:
            #查看乐谱 top
            #driver.find_elements_by_class_name('XCUIElementTypeButton')[2].click()
            driver.find_elements_by_accessibility_id('查看乐谱')[0].click()
            sleep(2)
        o=driver.find_elements_by_accessibility_id('好')
        if len(o)!=0:
            driver.find_element_by_accessibility_id('好').click()
        sleep(3)
        items=driver.find_elements_by_class_name('XCUIElementTypeCell')
        print('\nitems:'+str(len(items)))
        sleep(1)
        if (len(items)!=0 and len(flag)==0):
            driver.find_element_by_accessibility_id('查看乐谱').click()
            sleep(4)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_035b_beforeDelete_R.png'
            driver.save_screenshot(sf0)
            sleep(2)
            #自主上传
            self=driver.find_elements_by_accessibility_id('自主上传')
            if len(self)!=0:
                driver.find_element_by_accessibility_id('自主上传').click()
                sleep(2)
                driver.find_element_by_accessibility_id('编辑').click()
                sleep(2)
                driver.find_element_by_accessibility_id('ic drag').click()
                sleep(2)
                driver.find_element_by_accessibility_id('完成').click()
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='./'+now+'_035b_afterEdit_R.png'
                driver.save_screenshot(sf2)
                sleep(2)
            else:
                print('\n没有自主上传乐谱可以编辑！')
                sleep(2)
            driver.find_element_by_accessibility_id('删除').click()
            sleep(2)
            driver.find_element_by_accessibility_id('确定').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='./'+now+'_035b_afterDelete_R.png'
            driver.save_screenshot(sf4)
            sleep(2)
            items=driver.find_elements_by_class_name('XCUIElementTypeCell')
            print('\nafter deleting items:'+str(len(items)))
            sleep(1)
        elif (len(flag)!=0):
            print('\n现在时间不符合该脚本运行条件（课程已结束）!')
            sleep(1)
        elif (len(items)==0):
            print('\n现在没有乐谱可以删除/编辑!')
            sleep(1)
        else:
            print('\n发生未知原因错误，请检查!')
        sleep(2)
        driver.find_element_by_accessibility_id('ic nav back').click()
        sleep(3)
        driver.find_element_by_accessibility_id('个人中心').click()
        sleep(3)
        driver.swipe(500,500,0,-250,1000)
        sleep(2)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(3)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n035:非课程结束后删除/编辑曲谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('deleteEditMusicNotEnd'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_035b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版iOS9.3.3/iPhone5s真机(非课程结束后删除/编辑曲谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
