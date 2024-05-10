from apps.marketing.models import Banners


def get_banners(request):
    banners = Banners.objects.all()
    return {'banners': banners}
