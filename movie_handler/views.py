from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def detail(request, movie_title):
    movie = Movie.objects.get(title=movie_title)
    return render(request, "moviedetail.html", {"movie": movie})


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = Movie(title=form.cleaned_data["title"],
                            genre=form.cleaned_data["genre"],
                            release_year=form.cleaned_data["release_year"],
                            story_line=form.cleaned_data["story_line"]
                            )
            if form.cleaned_data["img"] is not None:
                new_doc.img = form.cleaned_data["img"]
            new_doc.save()
            return HttpResponseRedirect("/")
    else:
        form = MovieForm()
    return render(request, "add.html", {"form": form})


def delete_movie(request, movie_title):
    movie = Movie.objects.get(title=movie_title)
    movie.delete()
    return HttpResponseRedirect("/")
