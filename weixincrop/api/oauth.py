#!coding=utf-8
__author__ = '彤'
import urllib2
import urllib
import json
from django.http import HttpResponseRedirect
from common import getAccToken
from dvcrm.settings.base import WEIXIN_APPID,WEIXIN_CROPID

def oauth(redirect):
    token = getAccToken()
    redirect = urllib.quote_plus(redirect)
    api = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % (WEIXIN_CROPID,redirect)
    return HttpResponseRedirect(api)

def code2user(code):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=%s&code=%s' % token,code
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    return result['OpenId'],result['DeviceId']
