#!coding=utf-8
import urllib
import urllib2
import json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from dvcrm.settings.base import WEIXIN_APPID
from common import getAccToken

def check_file_size(type):
    return True

def create_tmp_media(type,file_path):
    token = getAccToken()
    register_openers()
    datagen, headers = multipart_encode({"media": open(file_path, "rb")})
    api = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s' % (token,type)
    req=urllib2.urlopen(api, datagen, headers)
    result = json.loads(req.read())
    return result['media_id']


def download_tmp_media(media_id,path):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s' % (token,media_id)
    try:
        urllib.urlretrieve(api, path)
        return True
    except Exception,e:
        print(unicode(e))
        return False

def create_longtime_media(type,file_path):
    token = getAccToken()
    register_openers()
    datagen, headers = multipart_encode({"media": open(file_path, "rb")})
    api = 'https://qyapi.weixin.qq.com/cgi-bin/material/add_material?agentid=%s&type=%s&access_token=%s' % (WEIXIN_APPID,type,token)
    req=urllib2.urlopen(api, datagen, headers)
    result = json.loads(req.read())
    return result['media_id']

def create_mpnews_message(article_list):
    token = getAccToken()
    data = {
        "agentid":WEIXIN_APPID,
        "mpnews":{
            "articles":article_list
        }
    }
    api = 'https://qyapi.weixin.qq.com/cgi-bin/material/add_material?agentid=%s&type=%s&access_token=%s' % WEIXIN_APPID,type,token
    req=urllib2.urlopen(api, data)
    result = json.loads(req.read())
    if result['errcode'] != '0':
        return False,result['errmsg']
    return True,result['media_id']

def update_mpnews_message(media_id,article_list):
    token = getAccToken()
    data = {
        "agentid":WEIXIN_APPID,
        "media_id":media_id,
        "mpnews":{
            "articles":article_list
        }
    }
    api = 'https://qyapi.weixin.qq.com/cgi-bin/material/update_mpnews?access_token=%s' % token
    req=urllib2.urlopen(api, data)
    result = json.loads(req.read())
    if result['errcode'] != '0':
        return False,result['errmsg']
    return True,result['media_id']


def delete_media(media_id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/material/del?access_token=%s&agentid=%s&media_id=%s' % token,WEIXIN_APPID,media_id
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != '0':
        return False,result['errmsg']
    return True,''

def media_count():
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/material/get_count?access_token=%s&agentid=%s' % token,WEIXIN_APPID
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    return result