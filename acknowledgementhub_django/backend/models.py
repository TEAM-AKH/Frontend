from django.db import models

# Create your models here.

class Products_data(models.Model):
    product_title = models.CharField(max_length=100)
    product_description = models.TextField()
    image = models.ImageField(upload_to='products/')
    social_media = models.URLField(max_length=200)
    CATEGORY_CHOICES = [
        ('AI-ML', 'AI-ML Products'),
        ('Cyber', 'Cyber Products'),
        ('General', 'General Products'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.product_title

class Events_data(models.Model):
    event_title = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField(null=True, blank=True) # Added event_date field
    image = models.ImageField(upload_to='events/', default='events/default.jpg')  # Added a default image
    social_media = models.URLField(max_length=200, default='#') # Added a default URL

    def __str__(self):
        return self.event_title