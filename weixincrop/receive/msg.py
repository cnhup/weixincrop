#!coding=utf-8
# from t4weixin.signals import *
from weixincrop.send.msg import data_to_xml
from weixincrop.signals import wxsignal_text, wxsignal_image, wxsignal_voice,\
    wxsignal_video, wxsignal_link, wxsignal_location

def process_text_msg(msg,server_host):
    data = wxsignal_text.send(sender='t4weixin',msg=msg,server_host=server_host)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})

def process_image_msg(msg,request):
    data = wxsignal_image.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})
    
def process_voice_msg(msg,request):
    data = wxsignal_voice.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})
    
def process_video_msg(msg,request):
    data = wxsignal_video.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})
    
def process_location_msg(msg,request):
    data = wxsignal_location.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})

def process_link_msg(msg,request):
    data = wxsignal_link.send(sender='t4weixin',msg=msg,request=request)
    if len(data) >= 1:
        for i in range(0,len(data)):
            if data[i][1]!=None:
                return data_to_xml(msg,data[i][1])
        return 'null'
    else:
        return data_to_xml(msg,{'MsgType':'text','Content':u'功能正在上线中，敬请等待'})


