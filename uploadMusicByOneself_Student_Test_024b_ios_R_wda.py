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
        print('\n024:自主上传乐谱----开始:'+now)
        sleep(1)

    def uploadMusicByOneself(self):
        login(self)
        sleep(3)
        s=c.session()
        if s(id='上节课程').exists:
            s(id='上节课程').tap()
            flag=s(className='XCUIElementTypeStaticText')[2].text
        else:
            flag=s(className='XCUIElementTypeStaticText')[3].text
        sleep(2)
        #ic upload1
        print('\n'+flag)
        print('\n已开始:'+str('已开始' in flag))
        print('\n已结束:'+str('已结束' in flag))
        sleep(1)
        if s(id='上传乐谱').exists:
            s(id='上传乐谱').tap()
        else:
            s(id='查看乐谱').tap()
        sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf='./'+now+'_024b_uploadedMusicIni_R.png'
        c.screenshot(sf)
        sleep(2)
        lis=s(className='XCUIElementTypeCell').find_elements()
        i=len(lis)
        print('\ni:'+str(i)+'----实际已有乐谱数量:'+str(i-1))
        sleep(2)
        #delete existing music
        if (i!=1 and (not ('已开始' in flag) and not ('已结束' in flag))):
            for j in range(i-1):
                s(id='删除').tap()
                sleep(2)
                s(id='确定').tap()
                sleep(2)
            sleep(2)
            s(id='上传乐谱').tap()
            sleep(2)
            """
            s(id='自主上传').tap()
            sleep(2)
            s(id='取消').tap()
            sleep(2)
            """
            s(id='自主上传').tap()
            sleep(2)
            s(id='最近上过的乐谱').tap()
            sleep(2)
            s(id='   添 加   ').tap()
            sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='./'+now+'_024b_uploadedMusicByBefore_R.png'
            c.screenshot(sf0)
            sleep(2)
            #[i] for not deleting firstly
            s(id='ic_next')[1].tap()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='./'+now+'_024b_uploadedMusicByBeforeDetail_R.png'
            c.screenshot(sf2)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
            s(id='上传乐谱').tap()
            sleep(2)
            s(id='自主上传').tap()
            sleep(2)
            s(id='从相册选择').tap()
            sleep(2)
            s(className='XCUIElementTypeButton')[7].tap()
            sleep(2)
            s(id='完成').tap()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='./'+now+'_024b_uploadedMusicByAlbum_R.png'
            c.screenshot(sf1)
            sleep(2)
            #[i+1] for not deleting firstly
            s(id='ic_next')[2].tap()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='./'+now+'_024b_uploadedMusicByAlbumDetail_R.png'
            c.screenshot(sf3)
            sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
            s(id='上传乐谱').tap()
            sleep(2)
            s(id='自主上传').tap()
            sleep(2)
            s(id='拍照上传').tap()
            sleep(2)
            s(id='ic_ photograph').tap()
            sleep(2)
            if s.alert.wait(3):
                s.alert.accept()
                sleep(2)
            s(xpath='//XCUIElementTypeButton[@name="FrontBackFacingCameraChooser"]').tap()
            sleep(3)
            #PhotoCapture
            s(id='PhotoCapture').tap()
            sleep(2)
            s(id='使用照片').tap()
            sleep(2)
            s(id='完成').tap()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='./'+now+'_024b_uploadedMusicBySelfie_R.png'
            c.screenshot(sf4)
            sleep(2)
            #[i+2] for not deleting firstly
            s(id='ic_next')[3].tap()
            sleep(8)
        else:
            s(id='上传乐谱').tap()
            sleep(2)
            s(id='自主上传').tap()
            sleep(2)
            s(id='取消').tap()
            sleep(2)
            s(id='自主上传').tap()
            sleep(2)
            s(id='最近上过的乐谱').tap()
            sleep(2)
            s(id='   添 加   ').tap()
            sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf5='./'+now+'_024b_uploadedMusicByBefore_R.png'
            c.screenshot(sf5)
            sleep(2)
            #[i] for not deleting firstly
            s(id='ic_next')[i].tap()
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf6='./'+now+'_024b_uploadedMusicByBeforeDetail_R.png'
            c.screenshot(sf6)
            sleep(2)
            turnpage_play(self)
            sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
            s(id='上传乐谱').tap()
            sleep(2)
            s(id='自主上传').tap()
            sleep(2)
            s(id='从相册选择').tap()
            sleep(2)
            s(className='XCUIElementTypeButton')[4].tap()
            sleep(2)
            s(id='完成').tap()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf7='./'+now+'_024b_uploadedMusicByAlbum_R.png'
            c.screenshot(sf7)
            sleep(2)
            #[i+1] for not deleting firstly
            s(id='ic_next')[i+1].tap()
            sleep(8)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf8='./'+now+'_024b_uploadedMusicByAlbumDetail_R.png'
            c.screenshot(sf8)
            sleep(2)
            s(id='ic nav back').tap()
            sleep(2)
            s(id='上传乐谱').tap()
            sleep(2)
            s(id='自主上传').tap()
            sleep(2)
            s(id='拍照上传').tap()
            sleep(2)
            s(id='ic_ photograph').tap()
            sleep(2)
            if s.alert.wait(3):
                s.alert.accept()
                sleep(2)
            s(xpath='//XCUIElementTypeButton[@name="FrontBackFacingCameraChooser"]').tap()
            sleep(2)
            #PhotoCapture
            s(id='PhotoCapture').tap()
            sleep(2)
            s(id='使用照片').tap()
            sleep(2)
            s(id='完成').tap()
            sleep(10)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf9='./'+now+'_024b_uploadedMusicBySelfie_R.png'
            c.screenshot(sf9)
            sleep(2)
            #[i+2] for not deleting firstly
            s(id='ic_next')[i+2].tap()
            sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf10='./'+now+'_024b_uploadedMusicBySelfieDetail_R.png'
        c.screenshot(sf10)
        sleep(2)
        s(id='ic nav back').tap()
        sleep(2)
        s(id='ic nav back').tap()
        sleep(2)
        logout(self)

    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n024:自主上传乐谱----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('uploadMusicByOneself'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_024b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(自主上传乐谱)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
