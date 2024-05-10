from django.contrib import admin
from .models import Banners


# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


admin.site.register(Banners, BannerAdmin)
