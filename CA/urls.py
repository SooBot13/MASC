from django.contrib import admin
from django.urls import path
from CA import views
urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("test",views.test, name='test')
]