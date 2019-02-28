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
        print('\n023:联系客服----开始:'+now)
        sleep(1)

    def callService(self):
        login(self)
        sleep(2)
        s=c.session()
        s(id='个人中心').tap()
        sleep(1)
        #ic customer
        s(id='呼叫客服').tap()
        sleep(2)
        s(id='呼叫').tap()
        sleep(1)
        s.alert.dismiss()
        sleep(2)
        s.swipe(800,500,800,280,0.5)
        sleep(2)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n023:联系客服----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('callService'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_023b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(联系客服)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
