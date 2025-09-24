from django.contrib import admin
from .models import Products_data, Events_data

class Products_dataAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'category', 'image', 'social_media')
    list_filter = ('category',)
    search_fields = ('product_title', 'product_description')

class Events_dataAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'image', 'social_media')
    search_fields = ('event_title', 'event_description')

admin.site.register(Products_data, Products_dataAdmin)
admin.site.register(Events_data, Events_dataAdmin)