'''
Created on 2014-6-17

@author: Administrator
'''
from django.http.response import HttpResponse
from weixincrop.receive.msg import process_text_msg, process_location_msg,\
    process_image_msg, process_voice_msg, process_video_msg, process_link_msg
from weixincrop.receive.event import process_subscribe_event, process_scan_event,\
    process_unsubscribe_event, process_location_event, process_click_event,\
    process_view_event

def proc_text(msg,server_host):
    return process_text_msg(msg,server_host)

def proc_location(msg,request):
    return process_location_msg(msg,request)

def proc_image(msg,request):
    return process_image_msg(msg,request)

def proc_voice(msg,request):
    return process_voice_msg(msg,request)

def proc_video(msg,request):
    return process_video_msg(msg,request)

def proc_link(msg,request):
    return process_link_msg(msg,request)

def proc_event(msg,request):
    eventType=msg.get("Event")
    proc_function = globals()["proc_%s"%eventType]
    if callable(proc_function):
        return proc_function(msg,request)
    else:
        return HttpResponse("EVENT ERROR")
#event_proc
def proc_subscribe(msg,request):
    return process_subscribe_event(msg,request)

def proc_unsubscribe(msg,request):
    return process_unsubscribe_event(msg,request)

def proc_SCAN(msg,request):
    return process_scan_event(msg,request)

def proc_LOCATION(msg,request):
    return process_location_event(msg,request)

def proc_CLICK(msg,request):
    return process_click_event(msg,request)

def proc_VIEW(msg,request):
    return process_view_event(msg,request)


