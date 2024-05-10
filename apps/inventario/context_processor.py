from apps.inventario.models import Categoria


def get_categorias(request):
    categorias = Categoria.objects.all()
    categorias_destacadas = Categoria.objects.filter(destacada=True)
    return {
        'categorias': categorias,
        'categorias_destacadas': categorias_destacadas
    }