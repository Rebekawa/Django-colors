# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to colors app")


color_list = ['blue', 'red', 'green']


def list(request):
    return HttpResponse(json.dumps(color_list), content_type="application/json")


def addColor(request):
    color = request.GET.get('colorname')
    if color in color_list:
        response_data = {'message': 'color {} is already in the list'.format(color)}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=409)
    elif color is None:
        return HttpResponse('Please add a color')
    else:
        color_list.append(color)
        return HttpResponse(json.dumps(color_list), content_type="application/json", status=201)


def getColor(request):
    color = request.GET.get('colorname')
    if color not in color_list:
        response_data = {'message': 'no such color'}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)
    return HttpResponse(color + ' is your color')
