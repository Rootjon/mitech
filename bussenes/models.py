from django.db import models

# Create your models here.

class Testimonial(models.Model):
    title=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='testimonial')

    def __str__(self):
        return self.title
    

class Demo(models.Model):
    title=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='demo')

    def __str__(self):
        return self.title
    
    
class Expert(models.Model):
    title=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    image=models.ImageField(upload_to='expert')
    social_facebook=models.URLField()
    social_github=models.URLField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='demo')

    def __str__(self):
        return self.title


class Brand(models.Model):
    image=models.ImageField(upload_to='brand')
    hover_image=models.ImageField(upload_to='brand')

class Award(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='awards')

    def __str__(self):
        return self.title

