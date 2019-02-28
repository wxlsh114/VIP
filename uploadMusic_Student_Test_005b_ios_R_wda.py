#coding=utf-8
import wda
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from pub_Student_wda import login,logout,turnpage_play

c=wda.Client('http://localhost:8100')

class TestStudent(unittest.TestCase):

    def setUp(self):
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n005:上传乐谱----开始:'+now)
        sleep(1)

    def uploadMusic(self):
        login(self)
        sleep(2)
        s=c.session()
        if s(id='上传乐谱').exists:
            s(id='上传乐谱').tap()
        else:
            s(id='查看乐谱').tap()
        sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_005b_beforeAddMusic_R.png'
        c.screenshot(sf0)
        sleep(2)
        s(id='上传乐谱').tap()
        sleep(2)
        s(id='钢琴').tap()
        sleep(2)
        s(id='小提琴').tap()
        sleep(2)
        s(id='手风琴').tap()
        sleep(2)
        s(id='钢琴').tap()
        sleep(2)
        s(id='搜索书名或者曲目名').tap()
        sleep(2)
        s(id='车尔尼').tap()
        sleep(2)
        s(id='包含该曲目').tap()
        sleep(2)
        #first music
        s(className='XCUIElementTypeCell')[0].tap()
        sleep(3)
        turnpage_play(self)
        sleep(1)
        s(id='ic nav back').tap()
        sleep(2)
        s(id='   添 加   ').tap()
        sleep(2)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='ic nav back').tap()
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_005b_afterAddMusic_R.png'
        c.screenshot(sf1)
        sleep(2)
        s(id='ic nav back').tap()
        sleep(2)
        logout(self)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n005:上传乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('uploadMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_005b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(上传乐谱)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
