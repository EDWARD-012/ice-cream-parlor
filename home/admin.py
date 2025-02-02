from django.contrib import admin
from home.models import Contact
from .models import Rating
# Register your models here.
admin.site.register(Contact)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'feedback', 'created_at')