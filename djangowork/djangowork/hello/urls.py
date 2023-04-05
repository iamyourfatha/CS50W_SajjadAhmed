from django.urls import path

from . import views #views.py and urls.py are in the same directory, so we can use "." for the "from"

urlpatterns = [
    path("", views.index, name="index"),
    path("sajjad", views.sajjad, name="sajjad"), 
    path("shah", views.shah, name="shah"),
    path("<str:name>", views.greet, name="greet")
]