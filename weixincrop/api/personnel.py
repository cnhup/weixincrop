#!coding=utf-8
import urllib2
import json
from common import getAccToken

def create_personnel(data):
    '''
    :param data:
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    print(result)
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,''


def update_personnel(data):
    '''

    :param data:
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,''


def delete_personnel(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=%s&userid=%s' % (token,id)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,''

def bulk_delete_personnel(id_list):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token=%s' % (token)
    req=urllib2.urlopen(api, json.dumps({'useridlist':id_list},ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,''

def list_unit_personnel(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=%s&userid=%s' % (token,id)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,result

def list_department_personnel(dep_id,fetch,status):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=%s&department_id=%s&fetch_child=%s&status=%s' % (token,dep_id,fetch,status)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,result['userlist']

def list_department_personnel_detail(dep_id,fetch,status):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=%s&department_id=%s&fetch_child=%s&status=%s' % (token,dep_id,fetch,status)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,result['userlist']


def invite_personnel(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/invite/send?access_token=%s' % (token)
    req=urllib2.urlopen(api, json.dumps({'userid':id},ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,''


def sync_personnel(data_list):
    print(data_list)
    for data in data_list:
        success,msg = create_personnel(data)
        print('create_personnel',success,msg)
        if not success:
            success,msg = update_personnel(data)
            print('update_personnel',success,msg)
    print('finish!')


