from wrapper import make_article
from ..api.message import send_news,send_text

def send_message2userlist(user_list,title,description,url,picurl=''):
    article = make_article(title,description,url,picurl)
    result,msg = send_news([article],user_list,[],[])
    print(result,msg)


def send_text2userlist(user_list,content):
    result,msg = send_text(content,user_list,[],[])
    print(result,msg)
