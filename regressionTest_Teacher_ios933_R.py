#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher_ios933 import login,logout,turnpage_play

import logIn_Teacher_Test_001b_ios933_R
import unsentClassSheet_Teacher_Test_002b_ios933_R
import searchMusic_Teacher_Test_003b_ios933_R
import checkSearchMusic_Teacher_Test_004b_ios933_R
import uploadMusic_Teacher_Test_005b_ios933_R
import checkHistoryClass_Teacher_Test_006b_ios933_R
import mySalary_Teacher_Test_007b_ios933_R
import testDevice_Teacher_Test_008b_ios933_R
import waitForStuMorethan1Min_Teacher_Test_009b_ios933_R
import aboutUs_Teacher_Test_010b_ios933_R
import generalSetting_Teacher_Test_011b_ios933_R
import logOut_Teacher_Test_012b_ios933_R
import uploadMusicFromClassroom_Teacher_Test_013b_ios933_R
import checkClassNote_Teacher_Test_014b_ios933_R
import bottomClassSheet_Teacher_Test_015b_ios933_R
import personalCenter_Teacher_Test_016b_ios933_R
import bottomMusic_Teacher_Test_017b_ios933_R
import advice_Teacher_Test_018b_ios933_R
import exitClassroom_Teacher_Test_019b_ios933_R
import switchLine_Teacher_Test_020b_ios933_R
import resetClassroom_Teacher_Test_021b_ios933_R
import waitForStudent_Teacher_Test_022b_ios933_R
import classUI_Teacher_Test_023b_ios933_R
import sentClassSheet_Teacher_Test_024b_ios933_R
import changePassword_Teacher_Test_025b_ios933_R
import callCustomerService_Teacher_Test_026b_ios933_R
import uploadMusicByOneself_Teacher_Test_027b_ios933_R
import displayAndPlayMusic_Teacher_Test_028b_ios933_R
import checkClassMusic_Teacher_Test_029b_ios933_R
import waitStuCheckClassNote_Teacher_Test_030b_ios933_R
import waitStuCheckMusic_Teacher_Test_031b_ios933_R
import uploadMusicByMeClassroom_Teacher_Test_032b_ios933_R
import searchMusicFromClassroom_Teacher_Test_033b_ios933_R
import deleteEditMusicAfterClassEnd_Teacher_Test_034b_ios933_R
import deleteEditMusicNotAfterClassEnd_Teacher_Test_035b_ios933_R

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestTeacher(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
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

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(logIn_Teacher_Test_001b_ios933_R.TestTeacher('Login'))
    testunit.addTest(unsentClassSheet_Teacher_Test_002b_ios933_R.TestTeacher('edit_send_Classshet'))
    testunit.addTest(searchMusic_Teacher_Test_003b_ios933_R.TestTeacher('searchMusic'))
    testunit.addTest(checkSearchMusic_Teacher_Test_004b_ios933_R.TestTeacher('checkSearchMusic'))
    testunit.addTest(uploadMusic_Teacher_Test_005b_ios933_R.TestTeacher('uploadMusic'))
    testunit.addTest(checkHistoryClass_Teacher_Test_006b_ios933_R.TestTeacher('checkHistoryClass'))
    testunit.addTest(mySalary_Teacher_Test_007b_ios933_R.TestTeacher('mySalary'))
    testunit.addTest(testDevice_Teacher_Test_008b_ios933_R.TestTeacher('testDevice'))
    testunit.addTest(waitForStuMorethan1Min_Teacher_Test_009b_ios933_R.TestTeacher('waitForStuMorethan1Min'))
    testunit.addTest(aboutUs_Teacher_Test_010b_ios933_R.TestTeacher('aboutUs'))
    testunit.addTest(generalSetting_Teacher_Test_011b_ios933_R.TestTeacher('generalSetting'))
    testunit.addTest(logOut_Teacher_Test_012b_ios933_R.TestTeacher('Logout'))
    testunit.addTest(uploadMusicFromClassroom_Teacher_Test_013b_ios933_R.TestTeacher('uploadMusicFromClassroom'))
    testunit.addTest(checkClassNote_Teacher_Test_014b_ios933_R.TestTeacher('checkClassNote'))
    testunit.addTest(bottomClassSheet_Teacher_Test_015b_ios933_R.TestTeacher('bottomClassshet'))
    testunit.addTest(personalCenter_Teacher_Test_016b_ios933_R.TestTeacher('personalCenter'))
    testunit.addTest(bottomMusic_Teacher_Test_017b_ios933_R.TestTeacher('bottomMusic'))
    testunit.addTest(advice_Teacher_Test_018b_ios933_R.TestTeacher('advice'))
    testunit.addTest(exitClassroom_Teacher_Test_019b_ios933_R.TestTeacher('exitClassroom'))
    #no such function now
    #testunit.addTest(switchLine_Teacher_Test_020b_ios933_R.TestTeacher('switchLine'))
    testunit.addTest(resetClassroom_Teacher_Test_021b_ios933_R.TestTeacher('resetClassroom'))
    testunit.addTest(waitForStudent_Teacher_Test_022b_ios933_R.TestTeacher('waitForStudent'))
    testunit.addTest(classUI_Teacher_Test_023b_ios933_R.TestTeacher('classUI'))
    testunit.addTest(sentClassSheet_Teacher_Test_024b_ios933_R.TestTeacher('sentClassSheet'))
    #025b moved to the end of this TestSuite 
    testunit.addTest(callCustomerService_Teacher_Test_026b_ios933_R.TestTeacher('callService'))
    testunit.addTest(uploadMusicByOneself_Teacher_Test_027b_ios933_R.TestTeacher('uploadMusicByOneself'))
    testunit.addTest(displayAndPlayMusic_Teacher_Test_028b_ios933_R.TestTeacher('displayPlayMusic'))
    testunit.addTest(checkClassMusic_Teacher_Test_029b_ios933_R.TestTeacher('checkClassMusic'))
    testunit.addTest(waitStuCheckClassNote_Teacher_Test_030b_ios933_R.TestTeacher('waitStuCheckClassNote'))
    testunit.addTest(waitStuCheckMusic_Teacher_Test_031b_ios933_R.TestTeacher('waitStuCheckMusic'))
    testunit.addTest(uploadMusicByMeClassroom_Teacher_Test_032b_ios933_R.TestTeacher('uploadMusicByOneselfClassr'))
    testunit.addTest(searchMusicFromClassroom_Teacher_Test_033b_ios933_R.TestTeacher('searchAddMusicClassroom'))
    testunit.addTest(deleteEditMusicAfterClassEnd_Teacher_Test_034b_ios933_R.TestTeacher('deleteEditMusicEnd'))
    testunit.addTest(deleteEditMusicNotAfterClassEnd_Teacher_Test_035b_ios933_R.TestTeacher('deleteEditMusicNotEnd'))
    testunit.addTest(changePassword_Teacher_Test_025b_ios933_R.TestTeacher('changePwd'))
    testunit.addTest(changePassword_Teacher_Test_025b_ios933_R.TestTeacher('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_regressionTest_ios933_003_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试老师版ios9.3.3/iPhone5s真机[回归测试+兼容性测试]测试报告by Appium',
                          description='自动化测试脚本集运行状态:')
    runner.run(testunit)
    fp.close()
