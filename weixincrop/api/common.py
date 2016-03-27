#!coding=utf-8
from django.core.cache import cache
from django.conf import settings
import datetime
import urllib2
import json
import requests
from urllib import quote
import math
from urllib2 import urlopen
#获取授权Token
def getAccToken():
    cropid = getattr(settings,'WEIXIN_CROPID')
    secret = getattr(settings,'WEIXIN_SECRET')
    
    if cache.get('WEIXIN_TOKEN_GETAT') == None or \
        (datetime.datetime.now() - cache.get('WEIXIN_TOKEN_GETAT')).seconds >= 7000:
        #重新获取token
        get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (cropid,secret)
        req = urllib2.Request(url=get_token_url)
        f = urllib2.urlopen(req)
        stringjson = f.read()
        accToken=json.loads(stringjson)['access_token']
        cache.set('WEIXIN_TOKEN', accToken,7200)
        cache.set('WEIXIN_TOKEN_GETAT',datetime.datetime.now(),10000)
        return accToken
    else:
        return cache.get('WEIXIN_TOKEN')


#拉取关注用户列表
def getWXUserList():
    TOKEN=getAccToken()
    url='https://api.weixin.qq.com/cgi-bin/user/get?access_token='+TOKEN
    res = urlopen(url)
    jsoncontent = json.loads(res.read())
    print jsoncontent
    
    


    
    
    
    
    
    
