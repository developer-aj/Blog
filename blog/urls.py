from django.conf.urls import patterns, include, url
from . import views
from mysite import settings

urlpatterns = patterns('',
	url(r'^$', views.main),
	url(r'^about/$', views.about),
	url(r'^contact/$', views.contact),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_edit"),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
