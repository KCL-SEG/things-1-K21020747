from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse("<title>Things</title>\n" + \
                            "<h1>Things<h1>")
    return response
