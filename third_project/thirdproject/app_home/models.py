from django.db import models

# Create your models here.


class Person(models.Model):

    COLOR_CHOICES = (
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('black', 'Black'),
)


    image = models.ImageField(upload_to='person-image',default='default.jpg')
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='green')
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=15,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)


    def __str__(self):
        return self.name