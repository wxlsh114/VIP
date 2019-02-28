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
        print('\n003:搜索添加乐谱库乐谱----开始:'+now)
        sleep(1)
        
    def searchMusic(self):
        login(self)
        sleep(3)
        #ic upload1
        s=c.session()
        if s(id='上传乐谱').exists:
            s(id='上传乐谱').tap()
        else:
            s(id='查看乐谱').tap()
        sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        s(id='上传乐谱').tap()
        #hot search
        s(id='搜索书名或者曲目名').tap()
        s(id='考级').tap()
        sleep(1)
        s(id='钢琴').tap()
        sleep(3)
        s(id='小提琴').tap()
        sleep(3)
        s(id='手风琴').tap()
        sleep(3)
        s(id='钢琴').tap()
        sleep(3)
        #first music
        s(className='XCUIElementTypeCell')[0].tap()
        sleep(3)
        #first item
        s(className='XCUIElementTypeCell')[0].tap()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_003b_searchedMusicByHotDetail_R.png'
        c.screenshot(sf2)
        sleep(2)
        turnpage_play(self)
        sleep(1)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='ic nav back').tap()
        sleep(1)
        """
        s(id='取消').tap()
        sleep(2)
        s(id='全部').tap()
        sleep(2)
        """
        #whole music name
        s(className='XCUIElementTypeTextField').tap()
        s(className='XCUIElementTypeTextField').set_text('车尔尼299 No.02')
        sleep(1)
        s(id='Search').tap()
        sleep(3)
        s(id='包含该曲目').tap()
        sleep(3)
        s(className='XCUIElementTypeCell')[0].tap()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_003b_searchedMusicByWholenameDetail_R.png'
        c.screenshot(sf1)
        sleep(2)
        turnpage_play(self)
        sleep(2)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='取消').tap()
        sleep(2)
        s(id='全部').tap()
        sleep(2)
        #keyword
        s(className='XCUIElementTypeTextField').tap()
        s(className='XCUIElementTypeTextField').set_text('299 No.07')
        sleep(1)
        s(id='Search').tap()
        sleep(3)
        s(id='包含该曲目').tap()
        sleep(3)
        s(className='XCUIElementTypeCell')[0].tap()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_003b_searchedMusicByKeywordDetail_R.png'
        c.screenshot(sf3)
        sleep(2)
        turnpage_play(self)
        sleep(1)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='取消').tap()
        sleep(2)
        s(id='ic nav back').tap()
        sleep(1)
        s(id='ic nav back').tap()
        sleep(2)
        logout(self)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n003:搜索添加乐谱库乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('searchMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_003b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(搜索添加乐谱库乐谱)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
