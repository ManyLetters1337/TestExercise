from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.
def product_list(request):
    """
    Product List View
    :param request:
    :return:
    """
    products = Product.objects.all()
    return render(request, 'product/products_list.html', {'products': products})


def product_detail(request, id):
    """
    Product Detail View
    :param request:
    :param id:
    :return:
    """
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/product.html', {'product': product})


