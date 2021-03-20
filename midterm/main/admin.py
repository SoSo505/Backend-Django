# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from main.models import Book,Journal, BookJournalBase

# Register your models here.
admin.site.register(Book)
admin.site.register(Journal)
admin.site.register(BookJournalBase)

