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
        print('\n018:投诉建议----开始:'+now)
        sleep(1)

    def advice(self):
        login(self)
        sleep(2)
        s=c.session()
        s(id='个人中心').tap()
        #s.swipe(700,500,700,50,0.5)
        #sleep(2)
        s(id='投诉建议').tap()
        sleep(1)
        s(className='XCUIElementTypeTextView').tap()
        s(className='XCUIElementTypeTextView').set_text('我的意见非常大，不是一句话能说完的。123456 abcdefg')
        sleep(1)
        s(id='提交').tap()
        sleep(3)
        s.swipe(800,500,800,280,0.5)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n018:投诉建议----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('advice'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_018b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(投诉建议)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
