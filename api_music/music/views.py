from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import AlbumSerializer, AlbumReviewSerializer
from rest_framework.exceptions import ValidationError


# Create your views here.

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer



class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Gali trinti ir redaguoti tik superuseris
    def delete(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError ("Only an administrator can delete!")

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError ("Only an administrator can edit!")


class AlbumReviewList(generics.ListCreateAPIView):
    # queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # Galima komentuot tik albuma kuri rodo
    def perform_create(self, serializer):
        album = Album.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_id=album)

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return AlbumReview.objects.filter(album_id=album)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("You can't delete strangers' posts!")

    def put(self, request, *args, **kwargs):
        review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("You can't update strangers' posts!")
