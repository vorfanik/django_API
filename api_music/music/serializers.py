from rest_framework import serializers
from .models import Album, AlbumReview, AlbumReviewLike, AlbumLike


class AlbumReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_id = serializers.ReadOnlyField(source='album.id')
    album = serializers.ReadOnlyField(source='album_id.name')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = AlbumReview
        fields = ['id', 'user_id', 'user_name', 'album_id', 'album', 'likes', 'content', 'score', 'created']

    def get_likes(self, like):
        return AlbumReviewLike.objects.filter(album_review_id=like).count()

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = ['id']


class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source='band_id.name')
    review = serializers.StringRelatedField(many=True)
    review_count = serializers.SerializerMethodField()
    songs = serializers.StringRelatedField(many=True)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Album
        fields = ['id', 'name', 'band_id', 'band_name', 'likes', 'review_count', 'songs', 'review', 'image']

    def get_review_count(self, review):
        return AlbumReview.objects.filter(album_id=review).count()

    def get_likes(self, like):
        return AlbumLike.objects.filter(album_id=like).count()


class AlbumLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumLike
        fields = ['id']
