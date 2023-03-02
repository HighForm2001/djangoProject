from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("hello world")

def user_list(request):
    return render(request, "user_list.html")

def tpl(request):
    name = "sdsd"
    ls = ["ceo","secure","tk"]
    return render(request, 'tpl.html',{"n2":name,"n3":ls})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.POST.get("username") == "root" and request.POST.get("pwd") == "123":
        return redirect("https://www.google.com")
    return render(request, "login.html", {"error":"wrong username or password"})

from app01.models import User
def orm(request):
    # delete
    # User.objects.all().delete()

    # create
    # User.objects.create(name="Chin",password="123",age=23)
    # User.objects.filter(id=1).delete()

    # get objects
    # data_list = User.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.name, obj.password)
    # row_obj = User.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name)

    # update
    # User.objects.filter(id=1).update(age=222)
    return HttpResponse("success")