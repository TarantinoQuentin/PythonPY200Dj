from django.urls import path
from .views import IndexView


urlpatterns = [
    path('landing/', IndexView.as_view(), name='index'),
]