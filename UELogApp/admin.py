# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from UELogApp.models import Resource, ResultRecord


# Register your models here.
admin.site.register(Resource)
admin.site.register(ResultRecord)