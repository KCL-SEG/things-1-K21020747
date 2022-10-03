from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse("<title>Things</title> \
                            <h1>Things<h1>")
    return response
