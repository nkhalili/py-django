# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pet

# Register your models here.
@admin.register(Pet)
class Admin(admin.ModelAdmin):
    # to change Pets columns and values in grid
    list_display = ['name', 'species', 'breed', 'age', 'sex']
