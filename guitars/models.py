from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    logo = models.ImageField(upload_to='images/logos')
    web_address = models.URLField(blank=True)

    def __str__(self):
        return self.name
