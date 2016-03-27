#!coding=utf-8
import urllib2
import json
from common import getAccToken

def create_tag(data):
    '''
    :param data:
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,''


def update_tag(data):
    '''

    :param data:
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,''


def delete_tag(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=%s&tagid=%s' % (token,id)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,''


def list_tag(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=%s' % (token)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,result['taglist']


def get_tag_personnel(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=%s&tagid=%s' % token,id
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,result['userlist']

def add_tag_personnel(data):
    '''
    {
       "tagid": "1",
       "userlist":[ "user1","user2"],
       "partylist": [4]
    }
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg'] + '-' + result['invalidlist'] + '-' + result['invalidparty']
    return True,''


def delete_tag_personnel(data):
    '''
    {
       "tagid": "1",
       "userlist":[ "user1","user2"],
       "partylist":[2,4]
    }
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg'] + '-' + result['invalidlist'] + '-' + result['invalidparty']
    return True,''


def sync_tag(data_list):
    for data in data_list:
        create_success,create_msg = create_tag(data)
        if not create_success:
            update_tag(data)