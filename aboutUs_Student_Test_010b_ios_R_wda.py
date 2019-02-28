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
        print('\n010:关于我们----开始:'+now)
        sleep(1)

    def aboutUs(self):
        login(self)
        sleep(4)
        s=c.session()
        s(id='个人中心').tap()
        s.swipe(800,500,800,50,0.5)
        sleep(2)
        s(id='关于我们').tap()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_010b_aboutUsTop_R.png'
        c.screenshot(sf0)
        sleep(2)
        s.swipe(800,600,800,50,0.5)
        sleep(1)
        s.swipe(800,600,800,50,0.5)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_010b_aboutUsMiddle_R.png'
        c.screenshot(sf2)
        sleep(2)
        s.swipe(800,600,800,50,0.5)
        sleep(1)
        s.swipe(800,600,800,50,0.5)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_010b_aboutUsTail_R.png'
        c.screenshot(sf1)
        sleep(2)
        s(id='ic nav back').tap()
        sleep(2)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n010:关于我们----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('aboutUs'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_010b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(关于我们)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
