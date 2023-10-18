from django.db import models

# Create your models here.
class ceos(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    first_year_active = models.CharField(max_length=256)
    def __str__(self):
        return self.name