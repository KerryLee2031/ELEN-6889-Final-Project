from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
import json
import requests
import random

def results(request):
    context = {}
    return render(request, "result.html", context)


def state_weather(request, state_name):
    context = {}
    context['state_weather'] = {
        "name": str(state_name)
    }

    return render(request,"weather.html", context)