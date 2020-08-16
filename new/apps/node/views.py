from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Kit
from django.urls import reverse

# Create your views here.

def home(request):
    status = Kit.objects.all()
    mystatus = status[0]
    param={"status":mystatus}
    return render(request, 'node/home.html',param)

def change(request):
    o = request.GET['light']
    print(o)
    status = Kit.objects.all()
    mystatus = status[0]
    if o == "Room1":
        r = mystatus.light1_status
        if r == "ON":
            mystatus.light1_status = "OFF"
            mystatus.save()
        elif r == "OFF":
            mystatus.light1_status = "ON"
            mystatus.save()
        else:
            print("Something Went Wrong inner")
    elif o=="Room2":
        r = mystatus.light2_status
        if r == "ON":
            mystatus.light2_status = "OFF"
            mystatus.save()
        elif r == "OFF":
            mystatus.light2_status = "ON"
            mystatus.save()
        else:
            print("Something Went Wrong inner")
    elif o == "Room3":
        r = mystatus.light3_status
        if r == "ON":
            mystatus.light3_status = "OFF"
            mystatus.save()
        elif r == "OFF":
            mystatus.light3_status = "ON"
            mystatus.save()
        else:
            print("Something Went Wrong inner")
    else:
        print("Something wrong outside")
    param={"status":mystatus}
    return HttpResponseRedirect(reverse('node:home'))

