from shop.order import Order
from shop.order_element import OrderElement


class ExpresssssOrder(Order):

    EXPRESS_DELIVERY_FEE = 10
    def __init__(self, delivery_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy(total_price) + ExpresssssOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        mark_line = '-' * 20
        order_details = f'Ekspresowe zamówienie złożone przez: {self.client_first_name} {self.client_last_name}'
        value_details = f'łączna wartość {self.total_price} PLN'
        delivery_date = f'z datą dostawy: {self.delivery_date}'
        product_details = 'Zamówione produkty: \n'
        for element in self._order_elements:
            product_details += f'\t{element}\n'
        result = '\n'.join([mark_line, order_details, value_details, delivery_date, product_details, mark_line])
        return result