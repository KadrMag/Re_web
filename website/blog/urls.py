from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:title>", views.post, name="post"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path('category/<str:name>', views.category, name="category"),
]
