from django.conf.urls import url
from Kiraya import views

urlpatterns = [
    url(r'^$',views.home, name="home"),
    url(r'^categories/$', views.categories, name="categories")
]
