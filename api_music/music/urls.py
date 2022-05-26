from django.contrib import admin
from django.urls import path
from .views import AlbumList, AlbumReviewList, AlbumDetail, AlbumReviewDetail, AlbumReviewLikeCreate, AlbumLikeCreate


urlpatterns = [
    path('album', AlbumList.as_view()),
    path('album/<int:pk>', AlbumDetail.as_view()),
    path('album/<int:pk>/review', AlbumReviewList.as_view()),
    path('album/<int:pk>/like', AlbumLikeCreate.as_view()),
    path('albumreview/<int:pk>', AlbumReviewDetail.as_view()),
    path('albumreview/<int:pk>/like', AlbumReviewLikeCreate.as_view()),
]
