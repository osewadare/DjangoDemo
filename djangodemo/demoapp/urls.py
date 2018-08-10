from django.conf.urls import url
from . import views

app_name = 'demoapp'

urlpatterns = [
    url(r'^$', views.indexview, name='index'),
    url(r'^list$', views.listview, name='list'),
    url(r'^add$', views.createStudent, name='add')
]