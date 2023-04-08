from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
#we need to move to 'wikiproj' venv
# /wikiproj/bin/activate 