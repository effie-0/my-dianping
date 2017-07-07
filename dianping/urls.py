from django.conf.urls import url
from . import views, myrequest

urlpatterns = [
    url(r'^$', views.index, name = 'index'),

    url(r'^search$', myrequest.search, name ='search'),
    url(r'^review_search$', myrequest.review_search, name ='review_search'),
    url(r'^multi_search$', myrequest.multi_search, name = 'multi_search'),
    url(r'^accurate/(.*)/$', myrequest.accurate, name = 'accurate'),

    url(r'^login$', views.login, name = 'login'),
    url(r'^authenticate$', views.authenticate, name = 'authenticate'),

    url(r'^signup$', views.signup, name = 'signup'),
    url(r'^signupsubmit$', views.signup_submit, name = 'signupsubmit'),

    url(r'^logout$', views.logout, name = 'logout'),
]