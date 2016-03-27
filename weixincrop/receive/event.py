#!coding=utf-8
import time

from django.dispatch.dispatcher import receiver

from weixincrop.signals import *
from weixincrop.send.msg import data_to_xml

def process_subscribe_event(msg,request):
    data = wxsignal_subscribe_event.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})


def process_unsubscribe_event(msg,request):
    data = wxsignal_unsubscribe_event.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})


def process_click_event(msg,request):
    data = wxsignal_click_event.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})


def process_view_event(msg,request):
    data = wxsignal_view_event.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})


def process_location_event(msg,request):
    print("start broadcast function")
    data = wxsignal_location_event.send(sender='t4weixin',msg=msg,request=request)
    print(data)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})

def process_scan_event(msg,request):
    data = wxsignal_scan_event.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})



    
    
    
    
    