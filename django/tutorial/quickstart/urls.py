from django.urls import path

from . import views


urlpatterns = [

    path("", views.index),

    path(
        "api/tts/",
        views.generate_tts
    ),

]