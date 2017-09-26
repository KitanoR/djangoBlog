from django.conf.urls import include,url #se agrega include
from . import views

urlpatterns = [
    url(r'^$',views.listar_pub, name='todas_pub'), #se redirecciona a la url del blog
    url(r'^postea/(?P<pk>[0-9]+)/$', views.detalle_pub, name = 'postea'), #se redirecciona a la url del blog
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^borradores/$', views.post_draft_list, name='post_draft_list'), # url para mostrar list
    url(r'^publicar/(?P<pk>\d+)/publish/$', views.publicar_post, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.eliminar_post, name='post_remove'),
]
