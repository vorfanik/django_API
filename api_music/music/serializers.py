from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike


class AlbumReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_id = serializers.ReadOnlyField(source='album.id')
    album = serializers.ReadOnlyField(source='album_id.name')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user_id', 'user_name', 'album_id', 'album', 'content', 'score', 'created']


class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source='band_id.name')
    review = serializers.StringRelatedField(many=True)
    review_count = serializers.SerializerMethodField()
    songs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'band_id', 'band_name', 'review_count', 'songs', 'review']

    def get_review_count(self, obj):
        return AlbumReview.objects.filter(album_id=obj).count()
