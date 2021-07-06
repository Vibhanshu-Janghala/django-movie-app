from django import forms


class MovieForm(forms.Form):
    title = forms.CharField(label="Title", max_length=240)
    release_year = forms.IntegerField(label="Release Year")
    genre = forms.CharField(label="Genre", max_length=255)
    story_line = forms.CharField(label="Plot Summary", max_length=1024, required=False)
    img = forms.ImageField(label="Image", required=False)
