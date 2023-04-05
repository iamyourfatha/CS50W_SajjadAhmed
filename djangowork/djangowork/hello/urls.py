from django.urls import path

from . import views #views.py and urls.py are in the same directory, so we can use "." for the "from"

urlpatterns = [
    path("", views.index, name="index")
]