from django.db import models
from django.db.models.base import Model
from django.urls import reverse

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

class Appointment(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Design(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='awards')

    def __str__(self):
        return self.title
    
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField()
    description=models.TextField()
    image=models.ImageField(upload_to='blog')
    creation=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("bussenes:details", kwargs={
            "slug": self.slug
            })
        
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
        
class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='album')

    def __str__(self):
        return self.title
    
class Contactus(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name