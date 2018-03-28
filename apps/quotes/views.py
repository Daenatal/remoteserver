# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Quotes
from django.contrib import messages
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'quotes/index.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)

        return redirect('/')

    if request.method == "POST":
        var1 = request.POST['password']
        var2 = request.POST['confirm']

    if var1 == var2:
        User.objects.create(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password'],
            birthday = request.POST['date']
        )
    return redirect('/')

def dashboard(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)

        return redirect('/')
    if request.method== "POST":
        request.session['user'] = str(request.POST['username'])
        varname = request.session.get('user')
        person = User.objects.get(username=varname)
        request.session['id'] = int(person.id)
        favs = request.session.get('favorite')
        context = {
            'profile': User.objects.get(username=str(request.POST['username'])),
            'quotes': Quotes.objects.all(),
        }
    else: 
        varname = request.session.get('user')
        favs = request.session.get('favorite')
        context= {
            'profile': User.objects.get(username=varname),
            'quotes': Quotes.objects.all(),
            'favorites': Quotes.objects.filter(name=favs),
        }

    return render(request, 'quotes/dashboard.html', context)

def add(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/dashboard')
    varname = request.session.get('user')
    person = request.session.get('id')
    if request.method == 'POST':
        Quotes.objects.create(
            name = request.POST['author'],
            content = request.POST['message'],
            poster = varname,
        )

        return redirect('/dashboard')
def show(request, name):
    varname = request.session.get('user')
    context = {
        'person': User.objects.get(username=name),
        'viewer': User.objects.get(username=varname),
        'lines': Quotes.objects.filter(poster=name),
        'count': Quotes.objects.filter(poster=name).count(),
    }
    return render(request, 'quotes/show.html', context)

def favorite(request, name):
    varname = request.session.get('user')
    request.session['favorite'] = name
    return redirect('/dashboard')