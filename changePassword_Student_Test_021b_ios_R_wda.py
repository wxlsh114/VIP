#coding=utf-8
import wda
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from pub_Student_wda import login,logout

c=wda.Client('http://localhost:8100')

class TestStudent(unittest.TestCase):

    def setUp(self):
        
        sleep(1)

    def changePwd(self):
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:修改密码----开始:'+now)
        login(self)
        sleep(2)
        s=c.session()
        s(id='个人中心').tap()
        sleep(1)
        s(id='修改密码').tap()
        sleep(1)
        s(className='XCUIElementTypeSecureTextField')[0].tap()
        s(className='XCUIElementTypeSecureTextField')[0].set_text('123456')
        sleep(1)
        s(xpath='//XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField').tap()
        s(xpath='//XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField').set_text('123456wxl')
        sleep(1)
        s(xpath='//XCUIElementTypeOther[3]/XCUIElementTypeSecureTextField').tap()
        s(xpath='//XCUIElementTypeOther[3]/XCUIElementTypeSecureTextField').set_text('123456wxl')
        sleep(1)
        s(id='确认').tap()
        sleep(3)
        s.swipe(800,500,800,280,0.5)
        sleep(2)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)
        s(id='登录').tap()
        sleep(1)
        #check new password
        s(className='XCUIElementTypeTextField').tap()
        s(className='XCUIElementTypeTextField').clear_text()
        s(className='XCUIElementTypeTextField').set_text('14100000011')
        sleep(1)
        s(className='XCUIElementTypeSecureTextField').tap()
        s(className='XCUIElementTypeSecureTextField').clear_text()
        s(className='XCUIElementTypeSecureTextField').set_text('123456wxl')
        sleep(1)
        #登 录
        s(className='XCUIElementTypeButton',name='登录').tap()
        sleep(8)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_021b_reLogin_R.png'
        c.screenshot(sf2)
        sleep(2)
        logout(self)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:修改密码----结束:'+now)
    
    def changePwdBack(self):
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:重置密码----开始:'+now)
        sleep(2)
        s=c.session()
        if s(id='个人中心').exists:
            s(id='个人中心').tap()
            s.swipe(800,500,800,280,0.5)
            sleep(2)
            s(id='退出登录').tap()
            s(id='确定').tap()
            sleep(1)
        s(id='登录').tap()
        s(className='XCUIElementTypeTextField').tap()
        s(className='XCUIElementTypeTextField').clear_text()
        s(className='XCUIElementTypeTextField').set_text('14100000011')
        s(className='XCUIElementTypeSecureTextField').tap()
        s(className='XCUIElementTypeSecureTextField').clear_text()
        s(className='XCUIElementTypeSecureTextField').set_text('123456wxl')
        s(className='XCUIElementTypeButton',name='登录').tap()
        #by_class_name('XCUIElementTypeButton')[2].click()
        sleep(5)
        #someone already logged in
        if s(id='确定').exists:
            s(id='确定').tap()
            sleep(2)
        if s.alert.wait(3):
            s.alert.accept()
            sleep(2)
        s(id='个人中心').tap()
        sleep(1)
        s(id='修改密码').tap()
        sleep(2)
        s(className='XCUIElementTypeSecureTextField')[0].tap()
        s(className='XCUIElementTypeSecureTextField')[0].set_text('123456wxl')
        sleep(1)
        s(xpath='//XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField').tap()
        s(xpath='//XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField').set_text('123456')
        sleep(1)
        s(xpath='//XCUIElementTypeOther[3]/XCUIElementTypeSecureTextField').tap()
        s(xpath='//XCUIElementTypeOther[3]/XCUIElementTypeSecureTextField').set_text('123456')
        sleep(1)
        s(id='确认').tap()
        sleep(3)
        s.swipe(800,500,800,280,0.5)
        sleep(2)
        s(id='退出登录').tap()
        s(id='确定').tap()
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('\n021:重置密码----结束:'+now)
        c.home()
            
    def tearDown(self):
        #c.home()
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestStudent('changePwd'))
    testunit.addTest(TestStudent('changePwdBack'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_021b_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试学生版iOS11.0.3/iPhone6真机(修改密码／重置密码)测试报告by WDA(Facebook)',
                          description='自动化测试脚本运行状态:')
    runner.run(testunit)
    fp.close()
