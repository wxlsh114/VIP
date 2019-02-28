#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout,turnpage_play

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestStudent(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'PRA-AL00'
        #desired_caps['udid'] = 'HMKNW17225011700'
        desired_caps['app'] = PATH('../VIPStudent_2.0.4.apk')
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass.pnlclass_student.ceshi'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def checkMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n004:查看乐谱----开始:'+now)
        login(self)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_004b_enteredUI_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        lis1=driver.find_elements_by_android_uiautomator('new UiSelector().text("课程表")')
        if len(lis1)==0:
            print('本周暂时没有课程安排!')
            sleep(2)
        else:
            flag=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvLine2').text
            print('\n'+flag)
            print('\n已开始:'+str('已开始' in flag))
            print('\n已结束:'+str('已结束' in flag))
            sleep(2)
            b=driver.find_elements_by_android_uiautomator('new UiSelector().text("上传乐谱")')
            if len(b)!=0:
                driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            else:
                driver.find_element_by_android_uiautomator('new UiSelector().text("查看乐谱")').click()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='./'+now+'_004b_classMuisc_R.png'
            driver.save_screenshot(sf1)
            sleep(2)
            #	com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvTitle
            items=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvTitle')
            i=len(items)
            print('\nitems:'+str(i))
            if i==1:
                print('本节课暂未上传乐谱')
                sleep(1)
            else:
                self=driver.find_elements_by_android_uiautomator('new UiSelector().text("自主上传乐谱")')
                if len(self)!=0:
                    driver.find_elements_by_android_uiautomator('new UiSelector().text("自主上传乐谱")')[0].click()
                    sleep(5)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='./'+now+'_004b_musicBySelfDetail_R.png'
                    driver.save_screenshot(sf1)
                    sleep(2)
                    page=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivNext')
                    if len(page)!=0:
                        driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivNext')[0].click()
                        sleep(2)
                        driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivLast')[0].click()
                        sleep(2)
                    driver.find_element_by_android_uiautomator('new UiSelector().text("编辑")').click()
                    sleep(3)
                    #	com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivDrag
                    driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivDrag').click()
                    sleep(2)
                    driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
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
                        driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
                        sleep(2)
                else:
                    driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvTitle')[1].click()
                    sleep(10)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='./'+now+'_004b_classMusicDetail_R.png'
                    driver.save_screenshot(sf2)
                    sleep(2)
                    #turn_pageAndplay
                    page=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivNext')
                    if len(page)!=0:
                        driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivNext')[0].click()
                        sleep(2)
                        driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/ivLast')[0].click()
                        sleep(2)
                    sleep(1)
                    #Add play code here
                    pb=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnPlayUrl')
                    if len(pb)!=0:
                        driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnPlayUrl').click()
                        sleep(8)
                        driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/btnPlayUrl').click()
                        sleep(2)
                    sleep(1)
                    driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
                    sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(2)
        driver.swipe(1000,1600,1000,1250,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n004:查看乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('checkMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_004_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)[查看乐谱]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
