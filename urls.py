from django.conf.urls import url
from . import views

app_name = 'HelloWORLD'
urlpatterns = [
    url(r'hw', views.hello, name='hello'),
    url(r'tsdb', views.testdb, name='testdb'),
    url(r'post', s)
]
