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
        print('\n019:退出教室:等待老师期间退出教室----开始:'+now)
        sleep(1)

    def exitClassroom(self):
        login(self)
        sleep(2)
        s=c.session()
        if s(id='本日暂时没有课程安排').exists:
            print('本日暂时没有课程安排!')
            sleep(3)
        else:
            s(id='进入教室').tap()
            sleep(5)
            if s(id='确定').exists:
                s(id='确定').tap()
                sleep(3)
            #'退出'
            s.tap(349,37)
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_019b_afterExitClassroom_R.png'
            c.screenshot(sf2)
            sleep(2)
        logout(self)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n019:退出教室:等待老师期间退出教室----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('exitClassroom'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_019b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(退出教室:等待老师期间退出教室)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
