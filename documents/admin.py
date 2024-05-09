from django.contrib import admin
from documents.models import Direction, New


# Register your models here.

@admin.register(Direction)
class DirectionsAdmin(admin.ModelAdmin):
    list_filter = ['type', 'faculty']
    list_display = ['title', 'type', 'faculty']


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
