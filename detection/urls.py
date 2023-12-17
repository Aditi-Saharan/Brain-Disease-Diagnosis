from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('result', views.result, name='result'),
    path('detect', views.detect, name='detect'),
    path('catalog', views.catalog, name='catalog'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup')

]