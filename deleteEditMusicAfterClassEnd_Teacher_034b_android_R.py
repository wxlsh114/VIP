#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher import login,logout,turnpage_play

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestTeacher(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'PRA-AL00'
        #desired_caps['udid'] = 'HMKNW17225011700'
        desired_caps['app'] = PATH('../VIPTeacher_2.0.3.apk')
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass_teacher.test'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def deleteEditMusicEnd(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n034:课程结束后删除/编辑曲谱----开始:'+now)
        login(self)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_034b_enteredUI_R.png'
        driver.save_screenshot(sf0)
        sleep(2)
        flag=driver.find_elements_by_android_uiautomator('new UiSelector().text("课程已结束")')
        if len(flag)!=0:
            print('\n课程已结束: True')
        else:
            print('\n课程已结束: False')
        sleep(1)
        lis1=driver.find_elements_by_android_uiautomator('new UiSelector().text("本日暂时没有课程安排")')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/courseCountTv')[i+1]
                if (bu.text!='0'):
                    bu.click()
                    sleep(2)
                    driver.find_element_by_android_uiautomator('new UiSelector().text("查看乐谱")').click()
                    sleep(3)
                    break
        else:
            driver.find_element_by_android_uiautomator('new UiSelector().text("查看乐谱")').click()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_034b_classMuisc_R.png'
        driver.save_screenshot(sf1)
        sleep(2)
        items=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/tvName')
        i=len(items)
        print('\nitems:'+str(i))
        sleep(1)
        if (i!=0 and len(flag)!=0):
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf='./'+now+'_034b_beforeDelete_R.png'
            driver.save_screenshot(sf)
            sleep(2)
            self=driver.find_elements_by_android_uiautomator('new UiSelector().text("自主上传乐谱")')
            if len(self)!=0:
                driver.find_elements_by_android_uiautomator('new UiSelector().text("自主上传乐谱")')[0].click()
                sleep(5)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='./'+now+'_034b_musicBySelfDetail_R.png'
                driver.save_screenshot(sf1)
                sleep(2)
                page=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/ivNext')
                if len(page)!=0:
                    driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/ivNext')[0].click()
                    sleep(2)
                    driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/ivLast')[0].click()
                    sleep(2)
                driver.find_element_by_android_uiautomator('new UiSelector().text("编辑")').click()
                sleep(3)
                #com.pnlyy.pnlclass_teacher.test:id/ivDrag
                driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/ivRotate').click()
                sleep(2)
                driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
                #sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='./'+now+'_034b_editNotAllowed_R.png'
                driver.save_screenshot(sf2)
                sleep(2)
                print('课程已结束后不允许编辑乐谱')
                sleep(2)
                driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
                sleep(2)
                driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
                sleep(2)
            else:
                print('没有自主上传乐谱可以编辑！')
                sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("删除")').click()
            sleep(2)
            driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/sureBtn').click()
            #sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_034b_delNotAllowed_R.png'
            driver.save_screenshot(sf2)
            sleep(2)
            print('课程已结束后不允许删除乐谱')
            sleep(2)
        elif (len(flag)==0):
            print('\n现在时间不符合该脚本运行条件!')
            sleep(1)
        elif i==0:
            print('\n本节课暂未上传乐谱，没有乐谱可以编辑或删除!')
            sleep(1)
        else:
            print('\n发生未知原因错误，请检查!')
            sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(3)
        driver.swipe(1000,1600,1000,1100,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n034:课程结束后删除/编辑曲谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('deleteEditMusicEnd'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_034b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[课程结束后删除/编辑曲谱]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
