#coding=utf-8
import wda
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from pub_Student_wda import login,logout

c=wda.Client('http://localhost:8100')

class TestStudent(unittest.TestCase):

    def setUp(self):
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n008:设备检测----开始:'+now)
        sleep(1)

    def testDevice(self):
        login(self)
        sleep(2)
        s=c.session()
        s(id='个人中心').tap()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_008b_personalCenter_R.png'
        c.screenshot(sf0)
        sleep(2)
        s(id='设备检测').tap()
        sleep(2)
        #test now
        s(id='开始测试').tap()
        s(id='点击开始录音').tap()
        sleep(2)
        s(id='停止录音').tap()
        s(id='有听到声音').tap()
        s(id='下一步').tap()
        s(id='下一步').tap()
        s(id='完成测试').tap()
        sleep(2)
        if s(id='已通过').exists:
            print('设备检测已通过')
        else:
            print('设备检测失败!')
        sleep(1)
        s.swipe(800,500,800,280,0.5)
        sleep(2)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)
        
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n008:设备检测----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('testDevice'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_008b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(设备检测)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
