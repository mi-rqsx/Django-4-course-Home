from django.shortcuts import render
from .models import Categories, Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug):
    good = Products.objects.get(slug=product_slug)

    context = {
        'good': good,
    }

    return render(request, 'goods/product.html', context=context)
