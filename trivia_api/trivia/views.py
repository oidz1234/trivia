from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings
import sys
sys.path.insert(0, str(settings.API_FUNC_DIR))
import capitals
import json


# Create your views here.
def index(request):
    return HttpResponse('<h1> It works! </h1>')


@api_view()
def test(request):
    print(settings.API_FUNC_DIR)
    print(settings.BASE_DIR)
    return Response({"message": "Hello, it is working!"})


@api_view()
def capital(request):
   question = capitals.get_capital_question()
   return Response(question)

