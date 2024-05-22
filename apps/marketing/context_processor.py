from apps.marketing.models import Banners, VideosPromocionales


def get_promociones(request):
    banners = Banners.objects.all()
    videos = VideosPromocionales.objects.filter(active=True)
    return {
        'banners': banners,
        'videos': videos
    }
