# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf


def product_introduction(request):  # index页面需要一开始就加载的内容写在这里
    context = {}
    return render(request, 'product_introduction.html', context)


def product_introduction_eng(request):  # index页面需要一开始就加载的内容写在这里
    context = {}
    return render(request, 'product_introduction_eng.html', context)
