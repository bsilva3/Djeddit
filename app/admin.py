from django.contrib import admin
from app.models import Topic, Comment, Post, Profile, Friend, Report

# Register your models here.

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Friend)
admin.site.register(Report)
