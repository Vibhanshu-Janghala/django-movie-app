from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
    path("<movie_title>", views.detail, name="movie_detail"),
    path("add/", views.add_movie, name="add_movie"),
    path("delete/<movie_title>", views.delete_movie, name="delete_movie")
]
urlpatterns += staticfiles_urlpatterns()
