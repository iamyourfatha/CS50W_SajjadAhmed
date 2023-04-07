from django.http import HttpResponseRedirect
from django.urls import reverse 
from django import forms
from django.shortcuts import render


class NewTaskForm(forms.Form): #the capitaliation of the F in Form matttered here
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] #on the right means its the value the variables takes on, its a python variable
        #on the left, its the name of the varbialbe that html can access
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            } )
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })