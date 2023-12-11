from collections.abc import Iterable
from django.db import models
from django.core.validators import FileExtensionValidator

TOO_BAD_CHOICE  = 1
BAD_CHOICE      = 2
NORMAL_CHOICE   = 3
GOOD_CHOICE     = 4
EXCELLENT_CHOICE= 5
RATING_CHOICES = [
    (TOO_BAD_CHOICE,"Too Bad"),
    (BAD_CHOICE,"Bad"),
    (NORMAL_CHOICE,"Normal"),
    (GOOD_CHOICE,"Good"),
    (EXCELLENT_CHOICE,"Excellent")
]






class Instructor(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES , default=NORMAL_CHOICE)
    #need a valdator here for postive foalt
    content = models.FloatField(default=0.0)



class Section(models.Model):
    title = models.CharField(max_length=100)
    #video field
    video_File = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','mov','wmv','flv','webm','mpeg','mpg'])])
    duration = models.FloatField(default=0.0)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    
class Course(models.Model):

    name = models.CharField(max_length=255)
    is_popular = models.BooleanField()
    is_trending = models.BooleanField()
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10,decimal_places=3)
    #video = models.FileField()
    #reviews
    rating = models.PositiveIntegerField(choices=RATING_CHOICES , default=NORMAL_CHOICE)
    #models.PROTECT is changable
    instructor = models.ManyToManyField(Instructor,related_name='coureses')
    number_of_hours = models.PositiveIntegerField(default=0)



class Customer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)