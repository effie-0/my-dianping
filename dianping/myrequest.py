from django.shortcuts import redirect, render
from .models import Business, Review

def search(request):
    #todo
    return render(request, 'display.html', {})




def review_search(request):
    # todo
    return render(request, 'display_review.html', {})

