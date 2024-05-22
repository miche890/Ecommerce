from django.contrib import admin
from .models import Banners, VideosPromocionales


# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Banners, BannerAdmin)


class VideosPromocionalesAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'active')


admin.site.register(VideosPromocionales, VideosPromocionalesAdmin)
