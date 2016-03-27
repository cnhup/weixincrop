#!coding=utf-8
import urllib2
import json
from common import getAccToken

def create_department(data):
    '''
    data的格式
    {
       "name": "广州研发中心",
       "parentid": "1",
       "order": "1",
       "id": "1"
    }
    :param data:
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))

    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,''


def update_department(data):
    '''

    :param data:
    :return:
    '''
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,''


def delete_department(id):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=%s&id=%s' % (token,id)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errcode']
    return True,''


def list_department(id=''):
    token = getAccToken()
    api = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=%s&id=%s' % (token,id)
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return result['department']


def sync_deparment(data_list):
    list_success,list_msg = now_deps = list_department()
    if not list_success:
        return False,list_msg
    now_ids = [item.id for item in now_deps ]
    msg = []
    success = True
    for data in data_list:
        if data.id in now_ids:
            update_success,update_msg = update_department(data)
            if not update_success:
                success = False
                msg.append(update_msg)
        else:
            create_success,create_msg = create_department(data)
            if not create_success:
                success = False
                msg.append(create_msg)

    return success,','.join(msg)

