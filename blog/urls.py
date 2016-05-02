from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^home/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),		
	url(r'^post/new/$', views.post_new, name='post_new'),		 			
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/junk/$', views.junkPost, name='junkPost'),
	url(r'^hello/$', views.viewName, name='hello'),
	url(r'^article/(\d+)/', views.viewArticle, name='article'),
	url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name='articles'),

]