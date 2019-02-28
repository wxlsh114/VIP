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
        print('\n002:等待老师进入（学生进入，老师未进入）---开始:'+now)
        sleep(1)

    def waitForTeacher(self):
        login(self)
        sleep(2)
        s=c.session()
        s(id='进入教室').tap()
        sleep(5)
        if s(id='确定').exists:
            s(id='确定').tap()
            sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_002b_enteredClassroom_R.png'
        c.screenshot(sf0)
        sleep(2)
        if s(id='pic_wait').exists:
            print('\nThere is a sign:请等待老师进入教室')
            sleep(2)
        s(id='呼叫老师').tap()
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_002b_afterCallTeacher_R.png'
        c.screenshot(sf1)
        sleep(2)
        s.tap(349,37)
        sleep(2)
        logout(self)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n002:等待老师进入（学生进入，老师未进入）----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('waitForTeacher'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_002b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(等待老师进入（学生进入，老师未进入）)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
