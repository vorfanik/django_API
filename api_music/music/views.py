from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import AlbumSerializer, AlbumReviewSerializer

# Create your views here.

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)