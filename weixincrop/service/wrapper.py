def make_mpnews(title,thumb_media_id,author,content_source_url,content,digest):
    return {
        "title": title,
        "thumb_media_id": thumb_media_id,
        "author": author,
        "content_source_url": content_source_url,
        "content": content,
        "digest": digest,
        "show_cover_pic": "0"
    }


def make_personnel(userid,name,mobile,gender,email,weixinid):
    data = {
        "userid": userid,
        "name": name,
        "department": [1,],
        "position":'',
        "extattr":{},
        "mobile": mobile,
        "gender": gender,
        "email": email,
        "weixinid": weixinid,
    }
    return data

def make_tag(name,id):
    data = \
        {
            "tagname": name,
            "tagid": id
        }
    return data


def make_article(title,description,url,picurl):
    return {
        "title": title,
        "description": description,
        "url": url,
        "picurl": picurl
    }
