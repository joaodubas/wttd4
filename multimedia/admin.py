from django.contrib import admin
from multimedia.models import Media

class MediaTabularInline(admin.TabularInline):
    model = Media
    extras = 1

