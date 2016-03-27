#!coding=utf-8
from common import getAccToken
from weixincrop.common import WEIXIN_RESPONSE_CODE
from dvcrm.settings.base import WEIXIN_APPID
from weixincrop.models import WMenu
import json
import urllib2

def sendmenu():
    access_token=getAccToken()
    # print access_token  cd ..
    posturl = "https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token=%s&agentid=%s" % (access_token,WEIXIN_APPID)

    menu = {'button':[]}

    def make_click(node):
        return {
                   'type':'click',
                   'name':node.name,
                   'key':node.value
                   }

    def make_view(node):
        return {
                   'type':'view',
                   'name':node.name,
                   'url':node.value
                   }

    for root in WMenu.objects.filter(parent=None).order_by('position'):
        if root.wtype == 'click':
            menu['button'].append(
                                  make_click(root)
                                  )
        elif  root.wtype == 'view':
            menu['button'].append(
                                  make_view(root)
                                  )
        elif root.wtype == 'parent':
            data = []
            for sub_node in WMenu.objects.filter(parent=root).order_by('position'):
                if sub_node.wtype == 'click':
                    data.append(
                                  make_click(sub_node)
                                  )
                elif  sub_node.wtype == 'view':
                    data.append(
                                  make_view(sub_node)
                                  )
            menu['button'].append(
                                  {
                                   'name':root.name,
                                   'sub_button':data
                                   }
                                  )
    print json.dumps(menu)
    req=urllib2.urlopen(posturl, json.dumps(menu,ensure_ascii=False).encode('utf-8'))

    result = json.loads(req.read())
    print('-----')
    print(result)
    if result['errcode'] != 0:
        return False, WEIXIN_RESPONSE_CODE[str(result['errcode'])]
    return True,''

def deletemenu():
    access_token=getAccToken()
    # print access_token  cd ..
    api = "https://qyapi.weixin.qq.com/cgi-bin/menu/delete?access_token=%s&agentid=%s" % access_token,WEIXIN_APPID
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,''

def listmenu():
    access_token=getAccToken()
    # print access_token  cd ..
    api = "https://qyapi.weixin.qq.com/cgi-bin/menu/get?access_token=%s&agentid=%s" % access_token,WEIXIN_APPID
    req=urllib2.urlopen(api)
    result = json.loads(req.read())
    if result['errcode'] != 0:
        return False, result['errmsg']
    return True,result