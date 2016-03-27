#!coding=utf-8
import json

from django.http import HttpResponse
from django.conf import settings

from xml.etree import ElementTree
from weixincrop.api import comprocs
from .lib.WXBizMsgCrypt import *
from weixincrop.service.query import get_server_host

def callback(request):  
    """
    微信的回调信息
    """
    # if True:
    server_host = get_server_host(request)
    signature = request.GET.get("msg_signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echoStr = request.GET.get("echostr", None)
    token = getattr(settings,'WEIXIN_TOKEN')
    aes_key = getattr(settings,'WEIXIN_AESKEY')
    cropid = getattr(settings,'WEIXIN_CROPID')
    wxcpt=WXBizMsgCrypt(token,aes_key,cropid)
    ret,sEchoStr=wxcpt.VerifyURL(signature, timestamp,nonce,echoStr)
    if request.body == "":
        return HttpResponse(sEchoStr)


    f = open('/tmp/wechat.txt',"w+")
    f.write('server_host:%s\t\n' % server_host)
    f.write('msg_signature:%s\r\n' % (signature))
    f.write('timestamp:%s\r\n' % (timestamp))
    f.write('nonce:%s\r\n' % (nonce))
    f.write('token:%s\r\n' % (token))
    f.write('aes_key:%s\r\n' % (aes_key))
    f.write('cropid:%s\r\n' % (cropid))
    f.write('body:\r\n%s\r\n' % (request.body))


    msg = {}
    ret,xml_content = wxcpt.DecryptMsg(request.body,signature,timestamp,nonce)
    f.write('ret:%s\r\n' % (ret))
    f.write('xml_content:\r\n%s\r\n' % (xml_content))



    xml_elem = ElementTree.fromstring(xml_content)


    if xml_elem.tag == 'xml':
        for child in xml_elem:
            msg[child.tag] = child.text

    f.write('msg:%s\r\n' % json.dumps(msg))

    msgType=msg.get("MsgType")
    proc_function = getattr(comprocs,"proc_%s" % msgType)

    f.write('proc_function:%s\r\n' % str(proc_function))

    if callable(proc_function):
        try:
            message = proc_function(msg,server_host)
        except Exception,e:
            f.write('call error:%s\r\n'% unicode(e))


        f.write('message_raw:%s\r\n' % str(message))

        ret,message = wxcpt.EncryptMsg(message,nonce,timestamp)

        f.write('message_encrypt:%s\r\n' % str(message))
        f.close()
        return HttpResponse(message)
    else:
        f.close()
        return HttpResponse("XML ERROR")
    

        



    
        
