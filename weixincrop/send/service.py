#!coding=utf-8
import json
import urllib2  
from weixincrop.api.common import getAccToken

def make_text_service(touser,content):
    """
    返回文本消息
    """
    return json.dumps({'touser':touser,
                       'msgtype':'text',
                       'text':{
                            "content":content
                           }})
    

def make_image_service(touser,imageid):
    pass

def make_voice_msg(media_id):
    pass

def make_video_msg(title,desc,media_id):
    pass

def make_music_msg(title,desc,music_url,hqmusic_url,thumb_media_id):
    pass

def make_news_item(touser,title,description,url,picurl):
    return json.dumps({
                "touser":touser,
                "msgtype":"news",
                "news":{
                    "articles": [
                     {
                         "title":title,
                         "description":description,
                         "url":url,
                         "picurl":picurl
                     }
                     ]
                        }
                 })
    
def make_news_msg(article_count,items):
    pass

def send_text_msg(touser,content):
    access_token=getAccToken()
    mess=make_text_service(touser,content)
    posturl = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + access_token
    urllib2.urlopen(posturl,mess)
    
def send_news_msg(touser,title,description,url,picurl):    
    access_token=getAccToken()
    mess=make_news_item(touser,title,description,url,picurl)
    posturl = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + access_token
    urllib2.urlopen(posturl,mess)
    
    
    
    
    