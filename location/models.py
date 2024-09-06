from django.contrib.gis.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)
