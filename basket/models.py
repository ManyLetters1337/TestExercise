from _decimal import Decimal
from product.models import Product
from shop import settings


class Basket(object):
    def __init__(self, request):
        """
        Init Basket
        :param request: Request Object
        """
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        """
        Iterator
        :return:
        """
        products_id = self.basket.keys()
        products = Product.objects.filter(id__in=products_id)
        for product in products:
            self.basket[str(product.id)]['product'] = product

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            yield item

    def add(self, product):
        """
        Add Product to Basket
        :param product: Product object
        :return:
        """
        if str(product.id) not in self.basket:
            self.basket[product.id] = {'price': str(product.price)}
        self.save()

    def save(self):
        """
        Save Basket in session
        :return:
        """
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def remove(self, product):
        """
        Remove Product from Basket
        :param product: Product object
        :return:
        """
        if str(product.id) in self.basket:
            del self.basket[str(product.id)]
            self.save()

    def __len__(self):
        """
        Get Product Count
        :return:
        """
        return len(self.basket.values())

    def clear(self):
        """
        Clear Basket
        :return:
        """
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        """
        Get total Price
        :return:
        """
        return sum(Decimal(item['price']) for item in self.basket.values())
