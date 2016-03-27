#!coding=utf-8
from django.db import models
import datetime
import time


class WMenu(models.Model):
    """
    微信菜单
    """
    WTYPE_CHOICES = (('click',u'点击'),
                     ('view',u'查看',),
                     ('parent',u'父菜单'))
    
    parent = models.ForeignKey('self',verbose_name=u'父菜单', null=True, blank=True, related_name='children')
    wtype = models.CharField(u'菜单类型',max_length=10,choices=WTYPE_CHOICES,help_text=u'类型为"父菜单",则必须要有子菜单')
    name = models.CharField(u'菜单名称',max_length=20)
    value = models.CharField(u'值',help_text=u'类型为"点击",则输入键码，如果类型为"查看",则输入url',max_length=256,null=True,blank=True)
    position = models.IntegerField(u'顺序')
    uuid = models.CharField(u"唯一标识符",max_length=20,null=True,blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name=u"微信菜单"
        verbose_name_plural=u"微信菜单管理"











        
        