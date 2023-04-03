from cgitb import html
from importlib.resources import contents
from lib2to3.pytree import convert
from turtle import title
from urllib import request
from django.shortcuts import render

from . import util
import markdown
import random


def convertor(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, title):
    html_content = convertor(title)
    if html_content == None :
        return render(request, "encyclopedia/error.html", {
            "massage" : "This page is not exsist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content" : html_content
        })
    

def search(request):
    if request.method == "POST":
        entry_search= request.POST['q']
        html_content = convertor(entry_search)
        if html_content is not None:
             return render(request, "encyclopedia/entry.html", {
                "title" : entry_search,
                "content" : html_content
            })
        else:
            allentries = util.list_entries()
            recomanded_s=[]
            for entry in allentries:
                if entry_search.lower() in entry.lower():
                 recomanded_s.append(entry)
            return render(request, "encyclopedia/search.html" , { 
            
                "recomanded_s" : recomanded_s
            })


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newp.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExsist = util.get_entry(title)
        if titleExsist is not None:
            return render(request, "encyclopedia/error.html", {
                "massage":"Entry Page Already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = convertor(title)
            return render(request, "encyclopedia/entry.html",{
                "title": title,
                "content": html_content
            })

def edit(request):
         if request.method == "POST":
            title = request.POST['entred_title']
            content = util.get_entry(title)
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content": content
            })

def save_newpage(request):
    if request.method =="POST":
        title=request.POST['title']
        content=request.POST['content']
        util.save_entry(title, content)
        html_content = convertor(title)
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
            })
         



def rande(request):
    allentries = util.list_entries()
    rande_entry = random.choice(allentries)
    html_content = convertor(rande_entry)
    return render(request, "encyclopedia/entry.html", {
        "title" : rande_entry,
        "content" : html_content
        

    })



