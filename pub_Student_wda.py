#coding=utf-8
import wda
import unittest,time,os
from time import sleep

#wda.DEBUG=True
c=wda.Client('http://localhost:8100')

def login(self):
    #print(c.status())
    s=c.session('com.Pnlyy.developmentVIPStudent')
    st=c.status() # json value
    assert st['state'] == 'success'
    sleep(5)
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
    #s(xpath='//XCUIElementTypeButton[@name="Toolbar Done Button"]').tap()
    s(className='XCUIElementTypeSecureTextField').tap()
    s(className='XCUIElementTypeSecureTextField').clear_text()
    s(className='XCUIElementTypeSecureTextField').set_text('123456')
    s(className='XCUIElementTypeButton',name='登录').tap()
    sleep(5)
    if s.alert.wait(3):
        s.alert.accept()
    sleep(2)
        
def logout(self):
    s=c.session()
    s(id='个人中心').tap()
    s.swipe(800,500,800,280,0.5)
    sleep(2)
    #s.tap(160, 465)
    s(id='退出登录').tap()
    s(id='确定').tap()
    sleep(1)
    #s.close()

def turnpage_play(self):
    s=c.session()
    sleep(1)
    #turn page left/right
    if s(id='ic next1').exists:
        s(id='ic next1')[0].tap()
        sleep(2)
        s(id='ic next2')[0].tap()
        sleep(2)
    sleep(1)
    #Add play code here
    if s(id='play').exists:
        s(id='play').tap()
        sleep(8)
        s(id='play').tap()
        sleep(2)
    sleep(1)
