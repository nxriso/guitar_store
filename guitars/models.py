from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='images/logos/')
    web_address = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Guitar(models.Model):
    ACOUSTIC = 'acoustic'
    ELECTRO_ACOUSTIC = 'electro_acoustic'
    ELECTRIC = 'electric'

    GUITAR_TYPE_CHOICES = (
        (ACOUSTIC, 'Acoustic'),
        (ELECTRO_ACOUSTIC, 'Electro-Acoustic'),
        (ELECTRIC, 'Electric'),
    )

    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    guitar_type = models.CharField(
        max_length=255,
        choices=GUITAR_TYPE_CHOICES,
        default=ACOUSTIC,
    )

    djent = models.BooleanField(default=False)
    image = ThumbnailerImageField('upload_to=images/guitar_model/')

    def __str__(self):
        return '%s %s' % (self.brand, self.model_name)
