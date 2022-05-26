from rest_framework import generics, permissions, mixins, status
from .models import Album, AlbumReview, AlbumReviewLike, AlbumLike
from .serializers import AlbumSerializer, AlbumReviewSerializer, AlbumReviewLikeSerializer, AlbumLikeSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


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
            raise ValidationError("Only an administrator can delete!")

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("Only an administrator can edit!")


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


class AlbumReviewLikeCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewLike.objects.filter(album_review_id=review, user=user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already like this post!')
        review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review_id=review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You haven't left a like after this post!")


class AlbumLikeCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = AlbumLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        album = Album.objects.get(pk=self.kwargs['pk'])
        return AlbumLike.objects.filter(album_id=album, user=user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already like this album!')
        album = Album.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_id=album)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You haven't left a like after this album!")
