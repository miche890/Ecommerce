from apps.marketing.models import Banners, VideosPromocionales


def get_promociones(request):
    banners = Banners.objects.all()
    videos = VideosPromocionales.objects.filter(active=True)
    banners_destacados = Banners.objects.filter(destacada=True)
    return {
        'banners': banners,
        'videos': videos,
        'banners_destacados': banners_destacados,
    }
