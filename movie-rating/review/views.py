from django.shortcuts import render, redirect
from django.views import generic
from .forms import ReviewForm
from .models import Review
import requests

def review_list(request):
    context = {'review_list': Review.objects.all(), 'movies': get_movies() }
    return render(request, "review/review_list.html", context)


def review_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ReviewForm()
        else:
            review = Review.objects.get(pk=id)
            form = ReviewForm(instance=review)
        return render(request, "review/review_form.html", {'form': form, 'movies': get_movies() })
    else:
        if id == 0:
            form = ReviewForm(request.POST)
        else:
            review = Review.objects.get(pk=id)
            form = ReviewForm(request.POST,instance=review)
        if form.is_valid():
            form.save()
        return redirect('/review/list')


def review_delete(request,id):
    review = Review.objects.get(pk=id)
    review.delete()
    return redirect('/review/list')


def get_movies():
    try:
        movies = requests.get("http://movie-provider:5000/movies").json().get("list")
    except:
        movies = []
    return movies

 
