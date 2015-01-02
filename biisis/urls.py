from django.conf.urls import patterns, url

from biisis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<biisi_id>\d+)/$', views.detail, name='detail'),
    url(r'create_biisi/', views.create_biisi, name="create_biisi"),
    url(r'^(?P<biisi_id>\d+)/change_laji/$', views.change_laji, name='change_laji'),
)