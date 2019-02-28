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
        print('\n020:登录成功后的课表界面----开始:'+now)
        sleep(1)

    def classUI(self):
        login(self)
        sleep(2)
        s=c.session()
        if s(id='本日暂时没有课程安排').exists:
            print('本日暂时没有课程安排!')
            sleep(2)
        else:
            if s(id='ic classroom2').enabled:
                print('进入教室的按钮现在是红色的!')
                sleep(2)
            else:
                print('进入教室的按钮现在是灰色的!')
                sleep(2)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_020b_classUI_R.png'
        c.screenshot(sf0)
        sleep(3)
        logout(self)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n020:登录成功后的课表界面----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('classUI'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_020b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(登录成功后的课表界面)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
