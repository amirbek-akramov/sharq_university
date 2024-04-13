from django.urls import path
from documents import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page')
]