#!coding=utf-8
import time
from lxml import etree
from weixincrop.lib.WXBizMsgCrypt import *

def response_xml(message):
    xml = etree.Element("xml")
    sub = etree.Element(key)
    sub.text= etree.CDATA(value)


def data_to_xml(msg,data):
    if 'ToUserName' not in data:
        data['ToUserName'] = msg['FromUserName']
    if 'FromUserName' not in data:
        data['FromUserName'] = msg['ToUserName']
    if 'CreateTime' not in data:
        data['CreateTime'] = int(time.time())

    xml = etree.Element("xml")

    def parsesub(key,value):
        if type(value) is str or type(value) is unicode:
            sub = etree.Element(key)
            sub.text= etree.CDATA(value)
            return sub
        if type(value) is int:
            sub = etree.Element(key)
            sub.text= '%d' % value
            return sub

        if type(value) is dict:
            sub = etree.Element(key)
            for sub_key,sub_value in value.items():
                sub.append(parsesub(sub_key,sub_value))
            return sub

        if type(value) is list:
            sub = etree.Element(key)
            for item in value:
                sub.append(parsesub('item',item))
            return sub

    for key,value in data.items():
        xml.append(parsesub(key,value))

    data = etree.tostring(xml,encoding='UTF-8')
    return data

def make_text_msg(content):
    """
    返回文本消息
    """
    return {'MsgType':'text','Content':content}

def make_image_msg(media_id):
    return {'MsgType':'image','Image':{'MediaId':media_id}}

def make_voice_msg(media_id):
    return {'MsgType':'voice','Voice':{'MediaId':media_id}}

def make_video_msg(title,desc,media_id):
    return {'MsgType':'video','Video':{'MediaId':media_id,'Title':title,'Description':desc}}

def make_music_msg(title,desc,music_url,hqmusic_url,thumb_media_id):
    return {'MsgType':'music','Music':{'Title':title,
                                       'Description':desc,
                                       'MusicUrl':music_url,
                                       'HQMusicUrl':hqmusic_url,
                                       'ThumbMediaId':thumb_media_id}}

def make_news_item(title,description,picurl,url):
    return {
        'title':title,
        'description':description,
        'picurl':picurl,
        'url':url
    }

def make_news_msg(article_count,items):
    return {'MsgType':'news',
            'ArticleCount':article_count,
            'Articles':[
                {
                    'Title':item['title'],
                    'Description':item['description'],
                    'PicUrl':item['picurl'],
                    'Url':item['url']
                }
                for item in items
            ]
    }

