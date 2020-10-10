from django.contrib import admin
from .models import Article, Contact
admin.site.register(Contact)
admin.site.register(Article)