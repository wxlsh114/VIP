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

    def deleteEditMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n025:非课程开始和结束后时间段删除/编辑曲谱----开始:'+now)
        login(self)
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
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_025b_classUI_R.png'
        driver.save_screenshot(sf)
        sleep(2)
        if (len(b)!=0 and (not ('已开始' in flag) and not ('已结束' in flag))):
            driver.find_element_by_accessibility_id('查看乐谱').click()
            sleep(2)
            ok=driver.find_elements_by_accessibility_id('好')
            if len(ok)!=0:
                driver.find_element_by_accessibility_id('好').click()
                sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_025b_beforeDelete_R.png'
            driver.save_screenshot(sf0)
            sleep(2)
            #item=driver.find_elements_by_class_name('XCUIElementTypeStaticText')[1].text
            #print(item)
            #sleep(1)
            edit=driver.find_elements_by_accessibility_id('自主上传乐谱')
            if len(edit)!=0:
                driver.find_element_by_accessibility_id('自主上传乐谱').click()
                sleep(2)
                driver.find_element_by_accessibility_id('编辑').click()
                sleep(2)
                #xy
                driver.find_element_by_accessibility_id('ic drag').click()
                sleep(2)
                driver.find_element_by_accessibility_id('完成').click()
                sleep(2)
            else:
                print('没有自主上传乐谱可以编辑！')
                sleep(2)
            driver.find_element_by_accessibility_id('删除').click()
            sleep(2)
            driver.find_element_by_accessibility_id('确定').click()
            sleep(4)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='./'+now+'_025b_afterDelete_R.png'
            driver.save_screenshot(sf4)
            sleep(2)
            driver.find_element_by_accessibility_id('ic nav back').click()
            sleep(2)
        elif (('已开始' in flag) or ('已结束' in flag)):
            print('现在时间不符合该脚本运行条件!')
            sleep(2)
        elif len(b)==0:
            print('没有乐谱可以删除/编辑!')
            sleep(2)
        else:
            print('发生未知原因错误，请检查!')
        sleep(2)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n025:非课程开始和结束后时间段删除/编辑曲谱----结束:'+now)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('deleteEditMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_025b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(非课程开始和结束后时间段删除/编辑曲谱)测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
