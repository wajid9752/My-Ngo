from django.contrib import admin
from .models import blog_category, blog, Event, Volunteer , Contact


@admin.register(blog_category)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_verified', 'pub_date_pretty']
    list_filter = ['category', 'is_verified']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'date_and_time', 'location', 'status']
    list_filter = ['event_type', 'status']

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']
   

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date_sent']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['date_sent']