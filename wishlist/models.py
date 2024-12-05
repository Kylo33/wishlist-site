from django.db import models

# Create your models here.

class Wishlist(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField()

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    label = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    modification_date = models.DateTimeField()

class WishlistItemLink(models.Model):
    wishlist_item = models.ForeignKey(WishlistItem, on_delete=models.CASCADE)

    label = models.CharField(max_length=200)
    link = models.URLField()