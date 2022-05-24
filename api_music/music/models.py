from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']


class Album(models.Model):
    name = models.CharField(max_length=100)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, Band: {self.band_id}"


class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, Album: {self.album_id}"


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    score = models.CharField(help_text="Format 1/10", max_length=5)

    def __str__(self):
        return f"Album {self.album_id}, User: {self.user}, Score: {self.score}"


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"User {self.user}, Album Review: {self.album_review_id}"


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user}, Album Review: {self.album_review_id}"