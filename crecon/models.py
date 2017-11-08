# -*- coding: utf-8 -*-
from django.db import models

class Salestring(models.Model):
    title = models.CharField(max_length=200)
    sumsale = models.FloatField()
    day_code = models.IntegerField()
    sale_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(models.Model):
    file_obj = models.FileField(upload_to='media/')

