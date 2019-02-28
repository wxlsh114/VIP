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

    def bottomMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n003:搜索添加乐谱库乐谱----开始:'+now)
        login(self)
        sleep(2)
        lis1=driver.find_elements_by_android_uiautomator('new UiSelector().text("课程表")')
        if len(lis1)==0:
            print('本周暂时没有课程安排!')
            sleep(2)
        else:
            b=driver.find_elements_by_android_uiautomator('new UiSelector().text("上传乐谱")')
            if len(b)!=0:
                driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            else:
                driver.find_element_by_android_uiautomator('new UiSelector().text("查看乐谱")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("搜索书名或曲目名")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("考级")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("钢琴")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("小提琴")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("手风琴")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("古筝")').click()
            sleep(2)
            #com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvMusicBookName
            driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvMusicBookName')[0].click()
            sleep(3)
            driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName')[0].click()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_003b_searchedMusicByHotDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("全部")').click()
            sleep(2)
            #keyword
            driver.find_element_by_android_uiautomator('new UiSelector().text("搜索书名或曲目名")').click()
            sleep(2)
            #com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etSearch2
            s=driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/etSearch2')
            s.click()
            s.set_value('299 No.07')
            sleep(1)
            #enter key=66
            driver.press_keycode(66)
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("包含该曲目")').click()
            sleep(2)
            #com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName
            driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName')[0].click()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_003b_searchedMusicByKeywordDetail_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n003:搜索添加乐谱库乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('bottomMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_003_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)[搜索乐谱并播放或查看]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
