from django.conf.urls import url
from . import views, myrequest

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^search$', myrequest.search, name ='search'),
    url(r'^review_search', myrequest.review_search, name ='review_search'),
    url(r'^multi_search', myrequest.multi_search, name = 'multi_search'),
    url(r'^accurate', myrequest.accurate, name = 'accurate'),
]