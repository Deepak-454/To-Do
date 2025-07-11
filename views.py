from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
def work(request):
    if request.method=="POST":
        task=request.POST
        if task:    
            Todo.objects.create(todo=task.get("task"),priority=task.get("priority"))
            messages.info(request,"Added")
        else:
            messages.info(request,"Please give some input")  
    sort=request.GET.get('sort')   
    if sort:     
        queryset=Todo.objects.filter(priority=sort)
    else:    
        queryset=Todo.objects.all()    
    return render(request,"List.html",context={"tasks":queryset})    
def remove_task(request,id):
    Todo.objects.get(id=id).delete()
    messages.info(request,"Removed")
    return redirect("/To-Do/") 
