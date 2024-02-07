from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    source_code = models.URLField()
    web_url = models.URLField()
    video = models.URLField()
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.firstname + " " + self.lastname