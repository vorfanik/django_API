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
    image = models.ImageField(upload_to='cover', null=True)

    def __str__(self):
        return f"{self.name}, Band: {self.band_id}"


class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return f"{self.name}, Album: {self.album_id}"


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='review')
    content = models.CharField(max_length=1000)
    score = models.CharField(help_text="Format 1/10", max_length=5)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" User: {self.user}, Review: {self.content}, Score: {self.score}, {self.created}"


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"User {self.user}, Album Review: {self.album_review_id}"


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"User {self.user}, Album Review: {self.album_review_id}"

class AlbumLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"User {self.user}, Album: {self.album_id}"
