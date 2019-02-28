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

    def uploadMusic(self):
        driver=self.driver
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:上传乐谱----开始:'+now)
        login(self)
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
            sf='./'+now+'_024b_classMuiscIni_R.png'
            driver.save_screenshot(sf)
            sleep(2)
            items=driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName')
            i=len(items)
            print('\nitems:'+str(i))
            sleep(1)
            
            #delete existing music
            if (i!=0 and (not ('已开始' in flag) and not ('已结束' in flag))):
                for j in range(i):
                    driver.find_element_by_android_uiautomator('new UiSelector().text("删除")').click()
                    sleep(3)
                    driver.find_element_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/sureBtn').click()
                    sleep(2)
                i=0
            sleep(2)
            
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
            sleep(3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("最近上过的乐谱")').click()
            sleep(2)
            add=driver.find_elements_by_android_uiautomator('new UiSelector().text("添加")')
            if len(add)!=0:
                driver.find_element_by_android_uiautomator('new UiSelector().text("添加")').click()
                sleep(2)
                #com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvMusicBookName
                driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName')[0].click()
                sleep(3)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='./'+now+'_024b_uploadedMusicByBeforeDetail_R.png'
                driver.get_screenshot_as_file(sf2)
                sleep(2)
                turnpage_play(self)
                sleep(2)
                k=1
                driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
                sleep(2)
            else:
                k=0
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_024b_uploadedMusicByBefore_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("从相册选择")').click()
            sleep(2)
            driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/indexTv')[3].click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByAlbum_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            #com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName
            print('\ni='+str(i)+'---k='+str(k)+'---i+k='+str(i+k))
            driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName')[i+k].click()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_024b_searchedMusicByKeywordDetail_R.png'
            driver.get_screenshot_as_file(sf0)
            sleep(2)
            #turnpage_play(self)
            #sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("上传乐谱")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("自主上传")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("拍照上传")').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
            sleep(4)
            driver.find_element_by_id('com.huawei.camera:id/shutter_button').click()
            sleep(2)
            #com.huawei.camera:id/btn_review_confirm
            driver.find_element_by_id('com.huawei.camera:id/btn_review_confirm').click()
            sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='./'+now+'_024b_uploadedMusicBySelfie_R.png'
            driver.get_screenshot_as_file(sf1)
            sleep(2)
            #for selfie
            #add codes here
            driver.find_elements_by_id('com.pnlyy.pnlclass.pnlclass_student.ceshi:id/tvName')[i+k+1].click()
            sleep(3)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicBySelfieDetail_R.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            #turnpage_play(self)
            #sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
            sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("返回")').click()
        sleep(3)
        logout(self)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:上传乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('uploadMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_024_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)[上传乐谱]测试报告by Appium',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
