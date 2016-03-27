#!coding=utf-8
import xadmin
from django.forms import ModelForm
from api.menu import sendmenu
from django.core.exceptions import ValidationError
from models import *
class WMenuAdmin(object):
    """
    """
    list_display = ('parent','name','wtype','value','position')
    list_display_links = list_display
    list_filter = ('wtype',)
    actions=['update_menu']

    def update_menu(self, request, queryset):
        result,code=sendmenu()
        if result!=True:
            self.message_user(request, u'%s' %code)
        else:
            self.message_user(request,u'菜单更新成功！')
    update_menu.short_description = "更新菜单到微信"

xadmin.site.register(WMenu,WMenuAdmin)
