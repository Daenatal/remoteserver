# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import m2m_changed

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        #checking everything for emptyness
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is required".format(field.replace('_', ''))
            if field == 'password':
                if not field in errors and len(value) < 8:
                    errors[field] = '{} field must be at least 8 characters'.format(field.replace('_', ''))
            if field == 'username':
                if not field in errors and len(value) < 5:
                    errors[field] = '{} field must be at least 5 characters'.format(field.replace('_', ''))
            if field == 'author':
                if not field in errors and len(value) < 3:
                    errors[field] = '{} field must be at least 3 characters'.format(field.replace('_', ''))
        return errors

#creating users table first
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
class Quotes(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    poster = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)