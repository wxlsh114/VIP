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

    def uploadMusicByOneself(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n027:自主上传乐谱----开始:'+now)
        login(self)
        sleep(2)
        lis1=driver.find_elements_by_android_uiautomator('new UiSelector().text("本日暂时没有课程安排")')
        if len(lis1)!=0:
            for i in range(6):
                bu=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/courseCountTv')[i+1]
                if (bu.text!='0'):
                    bu.click()
                    sleep(2)
                    #历史课单 middle
                    driver.find_element_by_android_uiautomator('new UiSelector().text("查看乐谱")').click()
                    sleep(2)
                    break
        else:
            driver.find_element_by_android_uiautomator('new UiSelector().text("查看乐谱")').click()
            sleep(2)
        o=driver.find_elements_by_android_uiautomator('new UiSelector().text("好")')
        if len(o)!=0:
            driver.find_element_by_android_uiautomator('new UiSelector().text("好")').click()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_027b_uploadedMusicItems_R.png'
        driver.get_screenshot_as_file(sf0)
        sleep(2)
        #com.pnlyy.pnlclass_teacher.test:id/rightTv
        items=driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/tvName')
        i=len(items)
        print('\nitems:'+str(i))
        sleep(1)
        if i==0:
            print('本节课暂未上传乐谱')
            sleep(1)
        else:
            for j in range(i-1):
                driver.find_element_by_android_uiautomator('new UiSelector().text("删除")').click()
                sleep(2)
                driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
                sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("最近上过的乐谱")').click()
            sleep(3)
            add=driver.find_elements_by_android_uiautomator('new UiSelector().text("添加")')
            if len(add)!=0:
                driver.find_element_by_android_uiautomator('new UiSelector().text("添加")').click()
                sleep(2)
            else:
                print('\n没有最近乐谱')
                sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_027b_uploadedMusicBybefore_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/tvName')[0].click()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='./'+now+'_027b_uploadedMusicByAlbeforeDetail_R.png'
            driver.get_screenshot_as_file(sf1)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("乐谱库")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("从相册选择")').click()
            sleep(3)
            #com.pnlyy.pnlclass_teacher.test:id/indexTv
            driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/indexTv')[3].click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
            sleep(6)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_027b_uploadedMusicByAlbum_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/tvName')[1].click()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_027b_uploadedMusicByAlbumDetail_R.png'
            driver.save_screenshot(sf2)
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("乐谱库")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("拍照上传")').click()
            sleep(3)
            allow=driver.find_elements_by_android_uiautomator('new UiSelector().text("始终允许")')
            if len(allow)!=0:
                driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
                sleep(3)
            #com.huawei.camera:id/shutter_button
            driver.find_element_by_id('com.huawei.camera:id/shutter_button').click()
            sleep(2)
            #com.huawei.camera:id/btn_review_confirm
            driver.find_element_by_id('com.huawei.camera:id/btn_review_confirm').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
            sleep(6)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='./'+now+'_027b_uploadedMusicBySelfie_R.png'
            driver.get_screenshot_as_file(sf4)
            sleep(2)
            driver.find_elements_by_id('com.pnlyy.pnlclass_teacher.test:id/tvName')[2].click()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf5='./'+now+'_027b_uploadedMusicBySelfieDetail_R.png'
            driver.get_screenshot_as_file(sf5)
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("乐谱库")').click()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf6='./'+now+'_027b_afterUploadedMusic_R.png'
            driver.get_screenshot_as_file(sf6)
            sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
        sleep(3)
        #退出
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n027:自主上传乐谱----结束:'+now)
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('uploadMusicByOneself'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_027b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[自主上传乐谱]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
