from django.shortcuts import render

# Create your views here.


def promociones(request):
    return render(request, 'marketing/index.html')
