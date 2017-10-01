from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^blog/(?P<blog_id>\d+)/$', get_one_blog, name='get_blog'),
    url(r'^add-blog/$', add_blog, name='add_blog'),
    url(r'^delete-blog/(?P<blog_id>\d+)/$', del_blog, name='del_blog'),
    url(r'^update-blog/(?P<blog_id>\d+)$', update_blog, name='update_blog'),
    url(r'^blogs/$', get_all_blog, name='get_all'),
    url(r'^$', base_page, name='base_page'),
]
