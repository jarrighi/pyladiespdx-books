from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.book_list_view),
    url(r'books/', views.book_list_view),
    url(r'^read/(?P<slug>[-\w]+)/$', views.book_detail_view),
)