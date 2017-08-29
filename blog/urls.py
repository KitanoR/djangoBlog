from django.conf.urls import include,url #se agrega include
from . import views

urlpatterns = [
    url(r'^$',views.listar_pub), #se redirecciona a la url del blog
]
