from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.urls import path
from django.http import HttpResponse
import os
@api_view(('GET',))
def directory(request):
    root = os.path.dirname(os.path.realpath(__file__))
    path = root + request.path
    os.chdir(path)
    return Response(os.listdir(path))

def parse(url):
    thlenght = len('create/')
    length = len(url)
    return url[0:length-thlenght]

def dparse(url):
    thlenght = len('download/')
    length = len(url)
    return url[0:length-thlenght]

@api_view(('GET',))
def createFolder(request):
    dirname = request.GET.get("fold")
    root = os.path.dirname(os.path.realpath(__file__))
    path = root + request.path
    os.chdir(parse(path))
    os.mkdir(parse(path) +  dirname)   
    return (Response(os.listdir(path='.')))

@api_view(('GET',))
def deleteFolder(request):
    dirname = request.GET.get("fold")
    root = os.path.dirname(os.path.realpath(__file__))
    path = root + request.path
    os.rmdir(parse(path) + dirname)   
    return (Response(os.listdir(path='.')))

@api_view(('GET',))
def download(request):
    filename = request.GET.get("file")
    root = os.path.dirname(os.path.realpath(__file__))
    path = dparse(root + request.path)
    pathToFile = os.path.join(path,filename) 
    file = open(pathToFile,"r") 
    response = HttpResponse(file,content_type='application/msword') 
    response['Content-Disposition'] = 'attachment; filename=' + filename 
    return response