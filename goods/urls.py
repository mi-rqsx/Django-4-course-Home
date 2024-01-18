from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    # path('<slug:category_slug>/<int:page>/', views.catalog, name='index'), # now we are using GET for pagination URL
    path('product/<slug:product_slug>/', views.product, name='product'),
]
