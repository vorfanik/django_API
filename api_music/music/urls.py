from django.contrib import admin
from django.urls import path
from .views import AlbumList, AlbumReviewList, AlbumDetail, AlbumReviewDetail


urlpatterns = [
    path('album', AlbumList.as_view()),
    path('album/<int:pk>', AlbumDetail.as_view()),
    path('album/<int:pk>/review', AlbumReviewList.as_view()),
    path('albumreview/<int:pk>', AlbumReviewDetail.as_view()),
]
