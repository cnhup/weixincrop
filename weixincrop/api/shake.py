#!coding=utf-8
__author__ = '彤'
import urllib2
import urllib
import json
from common import getAccToken
from dvcrm.settings.base import WEIXIN_APPID,WEIXIN_CROPID

def shake_ticket(redirect):
    token = getAccToken()
    redirect = urllib.urlencode(redirect)
    api = 'https://qyapi.weixin.qq.com/cgi-bin/shakearound/getshakeinfo?access_token=%s' % token
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    return result['ticket']

