from django.shortcuts import render
from django.http import HttpResponse
from post.models import *
from django.db.models import ObjectDoesNotExist
from django import template

from myBlog.settings import MEDIA_ROOT

# Create your views here.


def showPost(request,post_link):
    try:
        thisPost=post.objects.get(link=post_link)
        #s=str(thisPost.title)+"<br>"+str(thisPost.content)
        #s=s.replace('\n','<br>')
        return render(request,'post.html',{'post':thisPost})
    except ObjectDoesNotExist:
        return HttpResponse("Error: this post does not exist!")

def generateList(postList):
    List=[]
    for i in postList:
        item=[i,i.tags.all()]
        List.append(item)
    return List

def postIndex(request):
    postList=post.objects.all()
    #for i in postList:
    #    i.tags=i.tags.all()
    return render(request,'postList.html',{'postList':generateList(postList)})

def getPost(request):
    try:
        postName=request.GET.get('title','')
        s=post.objects.get(title=postName)
        return HttpResponse(s.content)
    except ObjectDoesNotExist:
        return HttpResponse("")