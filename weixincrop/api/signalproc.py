#!coding=utf-8
'''
Created on 2014-5-23

@author: Administrator
'''
import time
from django.dispatch.dispatcher import receiver
from weixincrop.signals import wxsignal_subscribe_event,\
    wxsignal_location_event, wxsignal_click_event
from weixincrop.models import User
from weixincrop.send.msg import data_to_xml, make_text_msg


@receiver(wxsignal_subscribe_event)
def process_subscribe_event(sender,**kwargs):
    tmpopenid=kwargs['msg']['FromUserName']
    userext=User.objects.filter(openid=tmpopenid)
    if userext.exists()==False:
        usertmp=User(openid=tmpopenid,subscribe_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        usertmp.save()

        



        
        

    