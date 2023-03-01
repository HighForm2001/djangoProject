from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("hello world")

def user_list(request):
    return render(request, "user_list.html")

def tpl(request):
    name = "sdsd"
    ls = ["ceo","secure","tk"]
    return render(request, 'tpl.html',{"n2":name,"n3":ls})