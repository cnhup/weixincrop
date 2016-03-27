#coding:utf8
import urllib2
import json
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login as django_login
from account.models import StaffUser,BaseUser
from weixincrop.api.oauth import oauth
from weixincrop.api.common import getAccToken


def get_full_path(request):
    return '%s://%s%s' % ('https' if request.is_secure() else 'http',request.get_host(),request.get_full_path())

def login_required(func):
    """
    要求登陆操作，登陆后自动跳转到登陆前的页面
    """
    def wrapper(request, *args, **kw):
        # return func(request, *args, **kw)
        print request.META['HTTP_USER_AGENT']
        if request.META.has_key('HTTP_USER_AGENT'):
            if request.META['HTTP_USER_AGENT'] != "MicroMessenger":
                if request.user is None:
                    return HttpResponseRedirect(reverse_lazy('mobile_login'))
                else:
                    return func(request,args,kw)


        cookie = request.COOKIES.get('userID','')
        code = request.GET.get('code','')
        if code != '':
            toke = getAccToken()
            api = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=%s&code=%s' % (toke,code)
            req=urllib2.urlopen(api)
            result = json.loads(req.read())
            if 'UserId' not in result:
                return HttpResponseRedirect('http://www.51xueyiedu.com/?from=UserId')
            userID = result['UserId']
            user = StaffUser.objects.get(user_id=userID).user
            user = authenticate(remote_user = user.username)
            if user is not None and user.is_active:
                django_login(request, user)
                return func(request, *args, **kw)
            else:
                return HttpResponseRedirect('http://www.51xueyiedu.com/?from=UserIsNotActive')

        if cookie == '':
            return oauth(get_full_path(request))
        user = BaseUser.objects.get(id=cookie)
        user = authenticate(remote_user = user.username)
        if user is not None and user.is_active:
            django_login(request, user)
            return func(request, *args, **kw)
        else:
            return oauth(get_full_path(request))
    return wrapper