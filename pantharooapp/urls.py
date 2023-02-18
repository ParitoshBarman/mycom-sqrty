from django.contrib import admin
from django.urls import path
from pantharooapp import views

urlpatterns = [
    path("", views.index, name='pantharooapp'),
    path("passingdataforsequrity/<int:empid>/<str:desktopname>/<str:ipADDress>/<str:fullname>/<str:email>/<str:now>/<str:appliName>", views.datacheak, name='pantharooapp'),
    path("passingfiledataforsequrity/<int:empid>/<str:desktopname>/<str:ipADDress>/<str:fullname>/<str:email>/<str:now>/<str:appliName>/<str:fileName>", views.fileNameDatacheak, name='pantharooapp')
]
