#coding=utf-8
import wda
import unittest,time,os,random
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from pub_Student_wda import login,logout

c=wda.Client('http://localhost:8100')

class TestStudent(unittest.TestCase):

    def setUp(self):
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n022:查看陪练单并评价老师----开始:'+now)
        sleep(1)

    def checkClassSheet(self):
        login(self)
        sleep(2)
        s=c.session()
        #bottom classSheet
        s(id='陪练单').tap()
        sleep(3)
        i=random.randrange(0,3,1)
        s(id='查看陪练单')[i].tap()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_022b_classSheetDetail1_R.png'
        c.screenshot(sf0)
        sleep(2)
        s.swipe(800,600,0,50,0.5)
        sleep(1)
        s.swipe(800,600,0,50,0.5)
        sleep(1)
        s.swipe(800,600,0,50,0.5)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_022b_classSheetDetail2_R.png'
        c.screenshot(sf1)
        sleep(2)
        if s(id='评价老师').exists:
            s(id='评价老师').tap()
            sleep(1)
            s(id='满意').tap()
            s(id='非常耐心').tap()
            s(id='声音甜美').tap()
            s(id='互动性强').tap()
            s(id='满意').tap()
            s.swipe(800,500,0,100,0.5)
            sleep(2)
            #without name
            s(className='XCUIElementTypeTextView').tap()
            s(className='XCUIElementTypeTextView').set_text('我的意见非常大，不是一句话能说完的。123456 abcdefg')
            sleep(1)
            s(id='完成').tap()
            s(id='提交评价').tap()
            sleep(3)
        s(id='ic nav back').tap()
        sleep(2)
        logout(self)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n022:查看陪练单并评价老师----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('checkClassSheet'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_022b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(查看陪练单并评价老师)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
