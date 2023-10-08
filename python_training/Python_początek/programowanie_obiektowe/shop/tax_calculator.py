

class TaxCalculator:

    FRUITS_AND_VEGATABLES = 0.05
    FOOD = 0.08
    ALL = 0.2

    @staticmethod
    def calculate_tax(order):
        for order_element in order._order_elements:
            amount = order_element.calculate_price

            if order_element.product.category_name == 'Owoce i warzywa':
                tax = amount * TaxCalculator.FRUITS_AND_VEGATABLES
            elif order_element.product.category_name == 'Jedzenie':
                tax = amount * TaxCalculator.FOOD
            else:
                tax = amount * TaxCalculator.ALL

            print(f'Kwota podatku dla pozycji: {order_element.product.name} w zamówieniu wynosi {tax:.2f} PLN')
            print(f"Całkowity koszt pozycji {order_element.product.name} wynosi {order_element.calculate_price + tax:.2f} PLN")
            print()

class Tax:

    TAX_RATES = {
        'Owoce i warzywa': 0.05,
        'Jedzenie': 0.08
    }
    BASE_TAX_RATE = 0.2

    @staticmethod
    def tax(order_element):
        product_category = order_element.product.category_name
        if product_category in Tax.TAX_RATES:
            tax_rate = Tax.TAX_RATES[product_category]
        else:
            tax_rate = Tax.BASE_TAX_RATE
        return tax_rate * order_element.calculate_price()
