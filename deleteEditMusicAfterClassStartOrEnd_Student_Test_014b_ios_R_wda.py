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
        print('\n014:课程开始和结束后删除/编辑曲谱----开始:'+now)
        sleep(1)

    def deleteEditMusicS(self):
        login(self)
        sleep(2)
        s=c.session()
        if s(id='上节课程').exists:
            s(id='上节课程').tap()
            flag=s(className='XCUIElementTypeStaticText')[2].text
        else:
            flag=s(className='XCUIElementTypeStaticText')[3].text
        sleep(2)
        #ic upload1
        print(flag)
        print('\n已开始:'+str('已开始' in flag))
        print('\n已结束:'+str('已结束' in flag))
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_014b_classUI_R.png'
        c.screenshot(sf)
        sleep(2)
        if ((s(id='查看乐谱').exists) and (('已开始' in flag) or ('已结束' in flag))):
            s(id='查看乐谱').tap()
            sleep(2)
            if s.alert.wait(3):
                s.alert.accept()
                sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_014b_beforeDelete_R.png'
            c.screenshot(sf0)
            sleep(2)
            if s(id='自主上传乐谱').exists:
                s(id='自主上传乐谱').tap()
                sleep(2)
                s(id='编辑').tap()
                sleep(2)
                s(id='ic drag').tap()
                sleep(2)
                s(id='完成').tap()
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='./'+now+'_014b_afterEdit_R.png'
                c.screenshot(sf2)
                sleep(2)
                #曲谱详情
                s(id='ic nav back').tap()
                sleep(1)
                s(id='ic nav back').tap()
                sleep(1)
            else:
                print('没有自主上传乐谱可以编辑！')
                sleep(2)
            if (not ('已开始' in flag)) and (not ('已结束' in flag)):
                s(id='删除').tap()
                sleep(2)
                s(id='确定').tap()
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf4='./'+now+'_014b_afterDelete_R.png'
                c.screenshot(sf4)
                sleep(2)
            else:
                print('\n课程已开始／已结束后不允许删除乐谱')
                sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
        elif (not ('已开始' in flag) or not ('已结束' not in flag)):
            #ic Sheet music
            print('\n现在时间不符合该脚本运行条件!')
            sleep(1)
        elif (not (s(id='查看乐谱').exists)):
            print('\n没有乐谱可以删除/编辑!')
            sleep(1)
        else:
            print('\n发生未知原因错误，请检查!')
        sleep(3)
        logout(self)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n014:课程开始和结束后删除/编辑曲谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('deleteEditMusicS'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_014b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(课程开始和结束后删除/编辑曲谱)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
