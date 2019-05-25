from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='info-home'),
    path('about/', views.about, name='info-about'),
]
