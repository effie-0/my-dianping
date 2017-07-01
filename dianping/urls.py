from django.conf.urls import url
from . import views, myrequest

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^search$', myrequest.search, name ='search'),
    url(r'^review_search', myrequest.review_search, name ='review_search'),
]