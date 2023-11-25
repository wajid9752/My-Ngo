from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils.text import slugify
import re
# Create your models here.


class blog_category(models.Model):
    category = models.CharField(max_length=50)
    category_img = models.ImageField(null=True , blank=True , upload_to="CategoryImg")
    description = models.CharField(max_length=250 , null=True , blank=True)
    def __str__(self):
        return self.category


class blog(models.Model):
    author =  models.ForeignKey(User , on_delete=models.CASCADE)
    short_caption = models.TextField(blank=True)
    title = models.CharField(max_length=250)
    mainImg = models.ImageField(null=True , blank=True , upload_to="BlogImg")
    description = HTMLField()
    category = models.ForeignKey(blog_category ,on_delete=models.CASCADE , related_name='blog_cat' )
    is_verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True , max_length=250 , blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def validate_slug(value):
        """
        Validate that the slug consists of letters, numbers, underscores, or hyphens.
        """
        if not re.match(r'^[-a-zA-Z0-9_]+$', value):
            raise ValidationError('Enter a valid slug consisting of letters, numbers, underscores, or hyphens.')
    
    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
    
    
    def cause_absolute_url(self):
        if self.slug:
            return reverse('blog:single-cause', kwargs={'slug': self.slug})
        return ''

    def get_absolute_url(self):
        if self.slug:
            return reverse('blog:single-blog', kwargs={'slug': self.slug})
        return ''
    




class Event(models.Model):
    EVENT_STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    event_name = models.CharField(max_length=255)
    description = HTMLField()
    date_and_time = models.DateTimeField()
    location = models.TextField()
    organizer = models.CharField(max_length=100)
    registration_deadline = models.DateTimeField()
    event_type = models.CharField(max_length=50)
    featured_image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default='upcoming')
    additional_information = HTMLField()

    def __str__(self):
        return self.event_name



class Volunteer(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    age = models.IntegerField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    availability = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name         = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email        = models.EmailField(blank=True)
    subject      = models.CharField(max_length=255 , blank=True)
    message     = models.TextField()
    date_sent   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"
