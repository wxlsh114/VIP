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
        print('\n015:课后陪练单----开始:'+now)
        sleep(1)

    def bottomClassSheet(self):
        login(self)
        sleep(3)
        s=c.session()
        #bottom classSheet
        s(id='陪练单').tap()
        sleep(1)
        s(id='查看陪练单').tap()
        sleep(6)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_015b_classSheetBottomTop_R.png'
        c.screenshot(sf0)
        sleep(2)
        s.swipe(800,500,800,50,0.5)
        sleep(1)
        s.swipe(800,500,800,50,0.5)
        sleep(1)
        s.swipe(800,500,800,50,0.5)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_015b_classSheetBottomTail_R.png'
        c.screenshot(sf1)
        sleep(2)
        if s(id='点击播放语音评价').exists:
            s(id='点击播放语音评价').tap()
            sleep(6)
            s(id='点击播放语音评价').tap()
            sleep(2)
        s(id='ic nav back').tap()
        sleep(3)
        logout(self)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n015:课后陪练单----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('bottomClassSheet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_015b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(课后陪练单)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
