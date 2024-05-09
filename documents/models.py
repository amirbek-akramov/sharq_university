from django.db import models


# Create your models here.

class Direction(models.Model):
    FACULTY_CHOICES = (
        ('Arxitektura va muxandislik fakulteti', 'ARCHITECT'),
        ('Axborot texnologiyalari (IT) va iqtisodiyot fakulteti', 'IT'),
        ('Sanoat va umumtexnika fakulteti', 'SVUT'),
        ('Ijtimoiy gumanitar fanlar va tillar fakulteti', 'HUMANITY')
    )

    TYPE_CHOICES = (
        ('BA', 'Bakalavr'),
        ('MA', 'Magistratura'),
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField()
    faculty = models.CharField(choices=FACULTY_CHOICES, max_length=53)
    daytime = models.PositiveIntegerField()
    externally = models.FloatField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=2)

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
