from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form): #the capitaliation of the F in Form matttered here
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks #on the right means its the value the variables takes on, its a python variable
        #on the left, its the name of the varbialbe that html can access
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })