from django.db import models
from django.contrib import admin

class User(models.Model):
    name = models.CharField(max_length=18, null=True)
    passwd = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.name

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','passwd')