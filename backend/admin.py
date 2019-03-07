# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from backend import models


admin.site.register(models.Permission)
admin.site.register(models.User)
admin.site.register(models.Role)

 #Register your models here.
