from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def detail(request, movie_title):
    movie = Movie.objects.get(title=movie_title)
    return render(request, "moviedetail.html", {"movie": movie})
