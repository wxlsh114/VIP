#coding=utf-8
import wda
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from pub_Student_wda import login,logout
#turnpage_play

import logIn_Student_Test_001b_ios_R_wda

import waitForTeacher_Student_Test_002b_ios_R_wda
import searchMusic_Student_Test_003b_ios_R_wda
import checkMusic_Student_Test_004b_ios_R_wda
import uploadMusic_Student_Test_005b_ios_R_wda
#import
import changeHeadIcon_Student_Test_007b_ios_R_wda
import testDevice_Student_Test_008b_ios_R_wda
#import
#import
import aboutUs_Student_Test_010b_ios_R_wda
import generalSetting_Student_Test_011b_ios_R_wda
import logOut_Student_Test_012b_ios_R_wda
#import
import deleteEditMusicAfterClassStartOrEnd_Student_Test_014b_ios_R_wda
import bottomClassSheet_Student_Test_015b_ios_R_wda
import personalCenter_Student_Test_016b_ios_R_wda
#import
import advice_Student_Test_018b_ios_R_wda
import exitClassroom_Student_Test_019b_ios_R_wda
import classUI_Student_Test_020b_ios_R_wda
import changePassword_Student_Test_021b_ios_R_wda
import checkClassSheet_Student_Test_022b_ios_R_wda
import callCustomerService_Student_Test_023b_ios_R_wda
import uploadMusicByOneself_Student_Test_024b_ios_R_wda
import deleteEditMusicNotAfterClassStartOrEnd_Student_Test_025b_ios_R_wda

c=wda.Client('http://localhost:8100')

class TestTeacher(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(logIn_Student_Test_001b_ios_R_wda.TestStudent('Login'))
    testunit.addTest(waitForTeacher_Student_Test_002b_ios_R.TestStudent('waitForTeacher'))
    testunit.addTest(searchMusic_Student_Test_003b_ios_R.TestStudent('searchMusic'))
    testunit.addTest(checkMusic_Student_Test_004b_ios_R.TestStudent('checkMusic'))
    testunit.addTest(uploadMusic_Student_Test_005b_ios_R.TestStudent('uploadMusic'))
    #006b
    testunit.addTest(changeHeadIcon_Student_Test_007b_ios_R.TestStudent('changeHeadIcon'))
    testunit.addTest(testDevice_Student_Test_008b_ios_R.TestStudent('testDevice'))
    #009b
    testunit.addTest(aboutUs_Student_Test_010b_ios_R_wda.TestStudent('aboutUs'))
    testunit.addTest(generalSetting_Student_Test_011b_ios_R.TestStudent('generalSetting'))
    testunit.addTest(logOut_Student_Test_012b_ios_R.TestStudent('Logout'))
    #013b
    testunit.addTest(deleteEditMusicAfterClassStartOrEnd_Student_Test_014b_ios_R.TestStudent('deleteEditMusicS'))
    testunit.addTest(bottomClassSheet_Student_Test_015b_ios_R.TestStudent('bottomClassSheet'))
    testunit.addTest(personalCenter_Student_Test_016b_ios_R.TestStudent('personalCenter'))
    #testunit.addTest(.TestStudent('bottomMusic'))
    testunit.addTest(advice_Student_Test_018b_ios_R.TestStudent('advice'))
    testunit.addTest(exitClassroom_Student_Test_019b_ios_R.TestStudent('exitClassroom'))
    testunit.addTest(classUI_Student_Test_020b_ios_R.TestStudent('classUI'))
    #021b moved to the end of this TestSuite
    testunit.addTest(checkClassSheet_Student_Test_022b_ios_R.TestStudent('checkClassSheet'))
    testunit.addTest(callCustomerService_Student_Test_023b_ios_R.TestStudent('callService'))
    testunit.addTest(uploadMusicByOneself_Student_Test_024b_ios_R.TestStudent('uploadMusicByOneself'))
    testunit.addTest(deleteEditMusicNotAfterClassStartOrEnd_Student_Test_025b_ios_R.TestStudent('deleteEditMusic'))
    testunit.addTest(changePassword_Student_Test_021b_ios_R.TestStudent('changePwd'))
    testunit.addTest(changePassword_Student_Test_021b_ios_R.TestStudent('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_regressionTest_001_R_wda.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机[回归测试]测试报告by WDA(Facebook)',
                          description='自动化测试脚本集运行状态:')
    runner.run(testunit)
    fp.close()
