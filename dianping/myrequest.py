from django.shortcuts import redirect, render
from .models import Business, Review

def search(request):
    request_type = request.POST.get("search_method")
    content = request.POST.get("request_content")
    if request.method == 'POST':

	    if request_type == '1':
	    	business_list = Business.objects.filter(name__contains = content)
	    elif request_type == '2':
	    	business_list = Business.objects.filter(popular_dishes__contains = content)
	    else:
	    	business_list = Business.objects.filter(address__contains = content)

    return render(request, 'display.html', {'businesses':business_list, })


def review_search(request):
    # todo
    return render(request, 'display_review.html', {})

def multi_search(request):
    #todo
    return render(request, 'display.html', {})

def accurate(request):
    if request.method == "POST":
        my_business = request.POST.get('business')
        my_reviews = business_review(my_business.shop_id)
        return render(request, 'show.html',
                      {'business': my_business, 'reviews' : my_reviews, })

def business_review(request_id):
    #todo
    reviews = []
    return reviews