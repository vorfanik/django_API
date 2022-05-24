from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'band_id']

class AlbumReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    user = serializers.ReadOnlyField(source='user.id')
    album = serializers.ReadOnlyField(source='album_id.name')
    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_name', 'album_id', 'album', 'content', 'score']
