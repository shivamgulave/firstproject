from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name="index"),
    # path("about/",views.about,name="about"),
    # path("service/",views.service,name="service"),
    # path("team/",views.team,name="team")

    ]   
