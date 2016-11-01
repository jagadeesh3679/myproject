from django.conf.urls import  url
from . import views
urlpatterns = [
    url(r'^h1/$',views.hello,name='hello'),
]
