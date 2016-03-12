from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)/$', views.single, name='single'),
	url(r'^new/$', views.new, name='new'),
	url(r'^user/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
	url(r'^$', views.index, name='index')
]
