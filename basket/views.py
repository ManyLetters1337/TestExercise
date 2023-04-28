from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST

from basket.models import Basket
from product.models import Product
from order.forms import OrderCreateForm
from order.models import OrderItem
from shop import settings


@require_POST
def basket_add(request, id):
    """
    Add Product to Basket
    :param request:
    :param id:
    :return:
    """
    basket = Basket(request)
    product = get_object_or_404(Product, id=id)
    if request.POST:
        basket.add(product)

    return redirect('basket:basket_detail')


def basket_remove(request, id):
    """
    Remove Product from Basket
    :param request:
    :param id:
    :return:
    """
    basket = Basket(request)
    product = get_object_or_404(Product, id=id)
    basket.remove(product)
    return redirect('basket:basket_detail')


def basket_detail(request):
    """
    Basket Detail Page
    :param request:
    :return:
    """
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            order.save_user_info(request)

            for item in basket:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'])
            basket.clear()

            return render(request, 'basket/order_completed.html',
                          {'order': order})
    else:
        user_info = request.session.get('user_info')
        if user_info:
            form = OrderCreateForm(initial={'phone': user_info['phone'], 'first_name': user_info['first_name'],
                                            'last_name': user_info['last_name'], 'address': user_info['address'],
                                            'city': user_info['city']})
        else:
            form = OrderCreateForm()

    return render(request, 'basket/detail.html', {'basket': basket, 'form': form})
