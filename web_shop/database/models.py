import datetime
from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    is_removed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='img', default='img/default-img.png')
    photo_preview = models.ImageField(
        upload_to='img/preview',
        default='img/preview/preview-default-img.png'
    )
    num_in_stock = models.IntegerField(default=0)

    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING
    )
    sub_category = models.ForeignKey(
        'SubCategory',
        on_delete=models.DO_NOTHING
    )
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def was_added_recently(self):
        return self.pub_date >= timezone.now() - \
            datetime.timedelta(days=1)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
