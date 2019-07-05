from django.urls import path

from . import views

urlpatterns = [
    path('ping', views.ping),
    path('feeds', views.FeedList.as_view()),
]
