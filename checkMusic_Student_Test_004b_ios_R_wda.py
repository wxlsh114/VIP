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
        print('\n004:查看乐谱----开始:'+now)
        sleep(1)

    def checkMusic(self):
        login(self)
        sleep(2)
        s=c.session()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_004b_classMuisc_R.png'
        c.screenshot(sf0)
        sleep(2)
        if s(id='上节课程').exists:
            s(id='上节课程').tap()
            flag=s(className='XCUIElementTypeStaticText')[2].text
        else:
            flag=s(className='XCUIElementTypeStaticText')[3].text
        sleep(2)
        #ic upload1
        #('查看乐谱')
        print('\n'+flag)
        print('\n已开始:'+str('已开始' in flag))
        print('\n已结束:'+str('已结束' in flag))
        sleep(2)
        if s(id='上传乐谱').exists:
            s(id='上传乐谱').tap()
        else:
            s(id='查看乐谱').tap()
        sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_004b_muiscItems_R.png'
        c.screenshot(sf)
        sleep(2)
        items=s(className='XCUIElementTypeCell').find_elements()
        i=len(items)
        print('items:'+str(i))
        if i==1:
            print('本节课暂未上传乐谱')
            sleep(1)
        else:
            if s(id='自主上传乐谱').exists:
                s(id='自主上传乐谱')[0].tap()
                sleep(5)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='./'+now+'_004b_musicBySelfDetail_R.png'
                c.screenshot(sf1)
                sleep(2)
                #turnpage_play(self)
                s.swipe(600,600,50,600,0.5)
                sleep(2)
                s.swipe(50,600,550,600,0.5)
                sleep(2)
                s(id='编辑').tap()
                sleep(2)
                s(id='ic drag').tap()
                sleep(2)
                s(id='完成').tap()
                sleep(2)
                if (not ('已开始' in flag)) and (not ('已结束' in flag)):
                    sleep(2)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='./'+now+'_004b_afterEdit_R.png'
                    c.screenshot(sf2)
                    sleep(2)
                else:
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='./'+now+'_004b_editNotAllowed_R.png'
                    c.screenshot(sf2)
                    sleep(2)
                    print('课程已开始／已结束后不允许编辑乐谱')
                    sleep(2)
                    s(id='ic nav back').tap()
                    sleep(2)
            else:
                s(id='ic_next')[1].click()
                sleep(10)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='./'+now+'_004b_classMusicDetail_R.png'
                c.screenshot(sf3)
                sleep(2)
                #turn page left/right and play music
                s.swipe(600,600,50,600,0.5)
                sleep(2)
                s.swipe(50,600,550,600,0.5)
                sleep(2)
                #Add play code here
                if s(id='play').exists:
                    s(id='play').tap()
                    sleep(8)
                    s(id='play').tap()
                    sleep(2)
                sleep(1)
                s(id='ic nav back').tap()
                sleep(2)
            if (not ('已开始' in flag)) and (not ('已结束' in flag)):
                s(id='删除').tap()
                sleep(2)
                s(id='确定').tap()
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf4='./'+now+'_004b_afterDelete_R.png'
                c.screenshot(sf4)
                sleep(2)
            else:
                print('\n课程已开始／已结束后不允许删除乐谱')
                sleep(2)
        s(id='ic nav back').tap()
        sleep(3)
        s(id='个人中心').tap()
        s.swipe(800,500,800,280,0.5)
        sleep(2)
        #s.tap(160, 465)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n004:查看乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('checkMusic'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_004b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(查看乐谱)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
