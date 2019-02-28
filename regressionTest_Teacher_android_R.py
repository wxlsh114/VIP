#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher import login,logout,turnpage_play

import logIn_Teacher_001b_android_R
import unsentClassSheet_Teacher_002b_android_R
import searchMusic_Teacher_003b_android_R
import checkSearchMusic_Teacher_004b_android_R
import uploadMusic_Teacher_005b_android_R
import checkHistoryClass_Teacher_006b_android_R
import mySalary_Teacher_007b_android_R
import testDevice_Teacher_008b_android_R
import waitForStuMorethan1Min_Teacher_009b_android_R
import aboutUs_Teacher_010b_android_R
import generalSetting_Teacher_011b_android_R
import logOut_Teacher_012b_android_R
import uploadMusicFromClassroom_Teacher_013b_android_R
import checkClassNote_Teacher_014b_android_R
import bottomClassSheet_Teacher_015b_android_R
import personalCenter_Teacher_016b_android_R
import bottomMusic_Teacher_017b_android_R
import advice_Teacher_018b_android_R
import exitClassroom_Teacher_019b_android_R
import switchLine_Teacher_020b_android_R
import resetClassroom_Teacher_021b_android_R
import waitForStudent_Teacher_022b_android_R
import classUI_Teacher_023b_android_R
import sentClassSheet_Teacher_024b_android_R
import changePassword_Teacher_025b_android_R
import callCustomerService_Teacher_026b_android_R
import uploadMusicByOneself_Teacher_027b_android_R
import displayAndPlayMusic_Teacher_028b_android_R
import checkClassMusic_Teacher_029b_android_R
import waitStuCheckClassNote_Teacher_030b_android_R
import waitStuCheckMusic_Teacher_031b_android_R
import uploadMusicByMeClassroom_Teacher_032b_android_R
import searchMusicFromClassroom_Teacher_033b_android_R
import deleteEditMusicAfterClassEnd_Teacher_034b_android_R
import deleteEditMusicNotAfterClassEnd_Teacher_035b_android_R

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

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(logIn_Teacher_001b_android_R.TestTeacher('Login'))
    testunit.addTest(unsentClassSheet_Teacher_002b_android_R.TestTeacher('edit_send_Classshet'))
    testunit.addTest(searchMusic_Teacher_003b_android_R.TestTeacher('searchMusic'))
    testunit.addTest(checkSearchMusic_Teacher_004b_android_R.TestTeacher('checkSearchMusic'))
    testunit.addTest(uploadMusic_Teacher_005b_android_R.TestTeacher('uploadMusic'))
    testunit.addTest(checkHistoryClass_Teacher_006b_android_R.TestTeacher('checkHistoryClass'))
    testunit.addTest(mySalary_Teacher_007b_android_R.TestTeacher('mySalary'))
    testunit.addTest(testDevice_Teacher_008b_android_R.TestTeacher('testDevice'))
    testunit.addTest(waitForStuMorethan1Min_Teacher_009b_android_R.TestTeacher('waitForStuMorethan1Min'))
    testunit.addTest(aboutUs_Teacher_010b_android_R.TestTeacher('aboutUs'))
    testunit.addTest(generalSetting_Teacher_011b_android_R.TestTeacher('generalSetting'))
    testunit.addTest(logOut_Teacher_012b_android_R.TestTeacher('Logout'))
    testunit.addTest(uploadMusicFromClassroom_Teacher_013b_android_R.TestTeacher('uploadMusicFromClassroom'))
    testunit.addTest(checkClassNote_Teacher_014b_android_R.TestTeacher('checkClassNote'))
    testunit.addTest(bottomClassSheet_Teacher_015b_android_R.TestTeacher('bottomClassSheet'))
    testunit.addTest(personalCenter_Teacher_016b_android_R.TestTeacher('personalCenter'))
    testunit.addTest(bottomMusic_Teacher_017b_android_R.TestTeacher('bottomMusic'))
    testunit.addTest(advice_Teacher_018b_android_R.TestTeacher('advice'))
    testunit.addTest(exitClassroom_Teacher_019b_android_R.TestTeacher('exitClassroom'))
    testunit.addTest(switchLine_Teacher_020b_android_R.TestTeacher('switchLine'))
    testunit.addTest(resetClassroom_Teacher_021b_android_R.TestTeacher('resetClassroom'))
    testunit.addTest(waitForStudent_Teacher_022b_android_R.TestTeacher('waitForStudent'))
    testunit.addTest(classUI_Teacher_023b_android_R.TestTeacher('classUI'))
    testunit.addTest(sentClassSheet_Teacher_024b_android_R.TestTeacher('sentClassSheet'))
    #025b moved to the end of this TestSuite 
    testunit.addTest(callCustomerService_Teacher_026b_android_R.TestTeacher('callService'))
    testunit.addTest(uploadMusicByOneself_Teacher_027b_android_R.TestTeacher('uploadMusicByOneself'))
    testunit.addTest(displayAndPlayMusic_Teacher_028b_android_R.TestTeacher('displayPlayMusic'))
    testunit.addTest(checkClassMusic_Teacher_029b_android_R.TestTeacher('checkClassMusic'))
    testunit.addTest(waitStuCheckClassNote_Teacher_030b_android_R.TestTeacher('waitStuCheckClassNote'))
    testunit.addTest(waitStuCheckMusic_Teacher_031b_android_R.TestTeacher('waitStuCheckMusic'))
    testunit.addTest(uploadMusicByMeClassroom_Teacher_032b_android_R.TestTeacher('uploadMusicByOneselfClassr'))
    testunit.addTest(searchMusicFromClassroom_Teacher_033b_android_R.TestTeacher('searchAddMusicClassroom'))
    testunit.addTest(deleteEditMusicAfterClassEnd_Teacher_034b_android_R.TestTeacher('deleteEditMusicEnd'))
    testunit.addTest(deleteEditMusicNotAfterClassEnd_Teacher_035b_android_R.TestTeacher('deleteEditMusicNotEnd'))
    testunit.addTest(changePassword_Teacher_025b_android_R.TestTeacher('changePwd'))
    testunit.addTest(changePassword_Teacher_025b_android_R.TestTeacher('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_regressionTest_newPara003_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版android7.0真机(Honor8Lite)[回归测试]测试报告by Appium',
                          description='自动化测试脚本集运行状态:')
    runner.run(testunit)
    fp.close()
