from django.contrib import admin
from george_app.models import *

admin.site.register(blogArticle)

class addArticle(admin.TabularInline):
    model = blogArticle
    fields = ['title', 'text', 'date', 'image', 'author_name']
    inlines = [fields]

