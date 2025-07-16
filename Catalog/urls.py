from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.main, name='index'),
    path('resume/', views.resume, name='resume'),

]
