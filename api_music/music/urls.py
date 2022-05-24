from django.contrib import admin
from django.urls import path
from .views import AlbumList, AlbumReviewList


urlpatterns = [
    path('album', AlbumList.as_view()),
    path('albumreview', AlbumReviewList.as_view()),
]