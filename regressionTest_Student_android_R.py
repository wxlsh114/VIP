#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
from pub_Student import login,logout,turnpage_play

import logIn_Student_001b_android_R
import waitForTeacher_Student_002b_android_R
import searchMusic_Student_003b_android_R
import checkMusic_Student_004b_android_R
import uploadMusic_Student_005b_android_R
#import
import changeHeadIcon_Student_007b_android_R
import testDevice_Student_008b_android_R
#import
import aboutUs_Student_010b_android_R
import generalSetting_Student_011b_android_R
import logOut_Student_012b_android_R
#import
import deleteEditMusicAfterClassStartOrEnd_Student_014b_android_R
import bottomClassSheet_Student_015b_android_R
import personalCenter_Student_016b_android_R
#import
import advice_Student_009b_android_R
import exitClassroom_Student_019b_android_R
import classUI_Student_020b_android_R
import changePassword_Student_021b_android_R
import checkClassSheet_Student_022b_android_R
import callCustomerService_Student_023b_android_R
import uploadMusicByOneself_Student_024b_android_R
import deleteEditMusicNotAfterClassStartOrEnd_Student_025b_android_R


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

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(logIn_Student_001b_android_R.TestStudent('Login'))
    testunit.addTest(waitForTeacher_Student_002b_android_R.TestStudent('waitForTeacher'))
    testunit.addTest(searchMusic_Student_003b_android_R.TestStudent('bottomMusic'))
    testunit.addTest(checkMusic_Student_004b_android_R.TestStudent('checkMusic'))
    testunit.addTest(uploadMusic_Student_005b_android_R.TestStudent('uploadMusic'))
    #006b
    testunit.addTest(changeHeadIcon_Student_007b_android_R.TestStudent('changeHeadIcon'))
    testunit.addTest(testDevice_Student_008b_android_R.TestStudent('testDevice'))
    testunit.addTest(advice_Student_009b_android_R.TestStudent('advice'))
    testunit.addTest(aboutUs_Student_010b_android_R.TestStudent('aboutUs'))
    testunit.addTest(generalSetting_Student_011b_android_R.TestStudent('generalSetting'))
    testunit.addTest(logOut_Student_012b_android_R.TestStudent('Logout'))
    #013b
    testunit.addTest(deleteEditMusicAfterClassStartOrEnd_Student_014b_android_R.TestStudent('deleteEditMusicS'))
    testunit.addTest(bottomClassSheet_Student_015b_android_R.TestStudent('bottomClassSheet'))
    testunit.addTest(personalCenter_Student_016b_android_R.TestStudent('personalCenter'))
    #017b,018b
    testunit.addTest(exitClassroom_Student_019b_android_R.TestStudent('exitClassroom'))
    testunit.addTest(classUI_Student_020b_android_R.TestStudent('classUI'))
    #021b moved to the end of this TestSuite
    testunit.addTest(checkClassSheet_Student_022b_android_R.TestStudent('checkClassSheet'))
    testunit.addTest(callCustomerService_Student_023b_android_R.TestStudent('callService'))
    testunit.addTest(uploadMusicByOneself_Student_024b_android_R.TestStudent('uploadMusic'))
    testunit.addTest(deleteEditMusicNotAfterClassStartOrEnd_Student_025b_android_R.TestStudent('deleteEditMusic'))
    testunit.addTest(changePassword_Student_021b_android_R.TestStudent('changePwd'))
    testunit.addTest(changePassword_Student_021b_android_R.TestStudent('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_regressionTest_newUI002_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版android7.0真机(Honor8Lite)',
                          description='自动化测试脚本集运行状态/[回归测试]测试报告by Appium:')
    runner.run(testunit)
    fp.close()
