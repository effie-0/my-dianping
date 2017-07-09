from django.conf.urls import url
from . import views, myrequest

urlpatterns = [
    url(r'^$', views.index, name = 'index'),

    url(r'^search$', myrequest.search, name ='search'),
    url(r'^review_search$', myrequest.review_search, name ='review_search'),
    url(r'^review_keyword$', myrequest.review_search_key_word, name = 'review_keyword'),
    url(r'^multi_search$', myrequest.multi_search, name = 'multi_search'),
    url(r'^accurate/(.*)/$', myrequest.accurate, name = 'accurate'),
    url(r'^recommend$', myrequest.recommend, name = 'recommend'),
    url(r'^create/(.*)/$', myrequest.create, name = 'create'),
    url(r'^home$', views.home, name = 'home'),
    url(r'^delete/(.*)/$', views.delete, name = 'delete'),
    url(r'^change/(.*)/$', views.change, name = 'change'),
    url(r'^changesubmit$', views.changesubmit, name = 'changesubmit'),
    url(r'^star/(.*)/$', views.changestar, name='star'),
    url(r'^region/(.*)/$', myrequest.region_search, name = 'region'),
    url(r'^dish/(.*)/$', myrequest.dish_search, name = 'dish'),

    url(r'^login$', views.login, name = 'login'),
    url(r'^authenticate$', views.authenticate, name = 'authenticate'),

    url(r'^signup$', views.signup, name = 'signup'),
    url(r'^signupsubmit$', views.signup_submit, name = 'signupsubmit'),

    url(r'^logout$', views.logout, name = 'logout'),
]