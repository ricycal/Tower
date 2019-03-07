# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
	
	
class User(models.Model):
    """ 用户表
        普通字段: id, username, password
        关联字段： roles(多对多)
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')

    roles = models.ManyToManyField(to='Role', verbose_name='角色', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户表'


class Permission(models.Model):
    """ 权限表
        普通字段: id, url, feature
    """
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=64, verbose_name='正则URL')
    feature = models.CharField(max_length=16, verbose_name='功能')

    def __str__(self):
        return self.feature

    class Meta:
        verbose_name_plural = '权限表'


class Role(models.Model):
    """ 角色表
        普通字段： id, ,title
        关联字段： permissions(多对多)
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=16, verbose_name='角色名')

    permissions = models.ManyToManyField(to='Permission', verbose_name='权限', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '角色表'

#标签表
class Tag(models.Model):
    name=models.CharField("标签名称",max_length=10)
    def __unicode__(self):
        return self.name
'''分类表
class Group(models.Model):
    name=models.CharField("群组名称",max_length=10)
    parent_id=models.IntegerField("父id")
    def __unicode__(self):
        return self.name'''
#文章表
class Article(models.Model):
    title=models.CharField("文章标题",max_length=30,blank=True)
    content=models.TextField("文章内容")
    author=models.ForeignKey(User,verbose_name="文章作者id")
    tag= models.ManyToManyField(Tag,verbose_name="标签")
# classify=models.ForeignKey(Group,verbose_name="分类id")
    browse=models.IntegerField("阅读量",default=0)
    status=models.IntegerField("文章状态，0：存在，1：已删除",default=0)
    update_time=models.DateTimeField("更新时间")
    create_time=models.DateTimeField("创建时间")
    def __unicode__(self):
        return self.title

# Create your models here.
