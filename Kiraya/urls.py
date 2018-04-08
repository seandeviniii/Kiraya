from django.conf.urls import url
from Kiraya import views

urlpatterns = [
    url(r'home/$',views.home, name="home"),
    url(r'categories/$', views.categories, name="categories"),
    url(r'offers/$',views.offers, name="offers")
]
