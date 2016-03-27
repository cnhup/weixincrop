#!coding=utf-8
__author__ = '彤'
import urllib2
import json
from common import getAccToken
from dvcrm.settings.base import WEIXIN_APPID

def userid2openid(userid):
    token = getAccToken()
    data = {
        "userid":userid,
        "agentid":WEIXIN_APPID
    }
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_openid?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))

    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg'],''
    return True,result['openid'],result['appid']

def openid2userid(openid):
    token = getAccToken()
    data = {
        "openid":openid
    }
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_userid?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))

    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg'],''
    return True,result['userid']
