from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks #on the right means its the value the variables takes on, its a python variable
        #on the left, its the name of the varbialbe that html can access
    })