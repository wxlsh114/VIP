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
        print('\n007:修改头像图片----开始:'+now)
        sleep(1)

    def changeHeadIcon(self):
        login(self)
        sleep(2)
        s=c.session()
        s(id='个人中心').tap()
        sleep(2)
        s(xpath='//XCUIElementTypeCell[1]/XCUIElementTypeImage[3]').tap()
        sleep(2)
        s(id='拍照').tap()
        sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        #FrontBackFacingCameraChooser
        s(xpath='//XCUIElementTypeButton[@name="FrontBackFacingCameraChooser"]').tap()
        sleep(3)
        #PhotoCapture
        s(id='PhotoCapture').tap()
        sleep(2)
        s(id='使用照片').tap()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf0='./'+now+'_007b_selfie_R.png'
        c.screenshot(sf0)
        sleep(2)
        s(xpath='//XCUIElementTypeCell[1]/XCUIElementTypeImage[3]').tap()
        sleep(2)
        s(id='从相册选择').tap()
        sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        s(id='相机胶卷').tap()
        sleep(2)
        s.tap(320,320)
        sleep(6)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_007b_selectedPhoto_R.png'
        c.screenshot(sf1)
        sleep(3)
        s.swipe(800,500,800,280,0.5)
        sleep(2)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)
    
    def tearDown(self):
        c.home()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n007:修改头像图片----结束:'+now)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('changeHeadIcon'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_007b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(修改头像图片)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
