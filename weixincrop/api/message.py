#!coding=utf-8
import json
import urllib2

from common import getAccToken
from dvcrm.settings.base import WEIXIN_APPID


def send_message(data):
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
    api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % token
    req=urllib2.urlopen(api, json.dumps(data,ensure_ascii=False).encode('utf-8'))
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg'] + '-' + result['invaliduser'] + '-' + result['invalidparty'] + '-' + result['invalidtag']
    return True,''


def send_text(content,to_user_list,to_department_list,to_tag_list):
    '''

    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "text",
            "agentid": WEIXIN_APPID,
            "text": {
                "content": content
            },
            "safe":"0"
        }
    return send_message(data)

def send_image(media_id,to_user_list,to_department_list,to_tag_list):
    '''

    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "text",
            "agentid": WEIXIN_APPID,
            "image": {
                "media_id": media_id
            },
            "safe":"0"
        }
    return send_message(data)


def send_voice(media_id,to_user_list,to_department_list,to_tag_list):
    '''

    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "text",
            "agentid": WEIXIN_APPID,
            "voice": {
                "media_id": media_id
            },
            "safe":"0"
        }
    return send_message(data)

def send_video(media_id,title,desc,to_user_list,to_department_list,to_tag_list):
    '''

    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "text",
            "agentid": WEIXIN_APPID,
            "video": {
                "media_id": media_id,
                "title": title,
                "description": desc
            },
            "safe":"0"
        }
    return send_message(data)

def send_file(media_id,to_user_list,to_department_list,to_tag_list):
    '''

    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "text",
            "agentid": WEIXIN_APPID,
            "file": {
                "media_id": media_id
            },
            "safe":"0"
        }
    return send_message(data)



def send_news(article_list,to_user_list,to_department_list,to_tag_list):
    '''

    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "news",
            "agentid": WEIXIN_APPID,
            "news": {
                "articles": article_list
            },
            "safe":"0"
        }
    return send_message(data)


def send_mpnews(article_list,to_user_list=[],to_department_list=[],to_tag_list=[]):
    '''
    :param data:
    :return:
    '''
    data = \
        {
            "touser": "|".join(to_user_list),
            "toparty": "|".join(to_department_list),
            "totag": "|".join(to_tag_list),
            "msgtype": "text",
            "agentid": WEIXIN_APPID,
            "news": {
                "articles": article_list
            },
            "safe":"0"
        }
    return send_message(data)
