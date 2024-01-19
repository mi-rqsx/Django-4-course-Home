from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Products
from .utils import q_search



def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

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
