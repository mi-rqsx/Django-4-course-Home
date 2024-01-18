from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Categories, Products



def catalog(request, category_slug):

    page = request.GET.get('page', 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'goods': current_page,
        'category_slug': category_slug, 
    }
    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug):
    good = Products.objects.get(slug=product_slug)

    context = {
        'good': good,
    }

    return render(request, 'goods/product.html', context=context)
