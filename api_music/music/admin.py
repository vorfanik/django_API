from django.contrib import admin
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike, AlbumLike

# Register your models here.

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReviewLike)
admin.site.register(AlbumLike)