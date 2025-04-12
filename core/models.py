from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.IntegerField(default=100)
    agenda = models.TextField(blank=True, null=True)
    what_you_will_learn = models.TextField(blank=True, null=True)
    
    # For event speakers
    speakers = models.ManyToManyField('Speaker', related_name='events', blank=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_upcoming(self):
        return self.date > timezone.now()
    
    def save(self, *args, **kwargs):
        # Generate slug from title if not provided
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.event.title}"

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"Image in {self.gallery.title}"

class Solution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    features = models.TextField()
    image = models.ImageField(upload_to='solutions/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    
    def __str__(self):
        return f"Testimonial from {self.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name}: {self.subject}"

class DemoRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    
    def __str__(self):
        return f"Demo request from {self.name} ({self.company})"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    
    def __str__(self):
        return self.title
