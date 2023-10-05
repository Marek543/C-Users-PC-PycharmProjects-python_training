
class Discount:

    REGULAR_CUSTOMER = 0.05
    HOLIDAY_SPECIAL = 20

    @staticmethod
    def no_discount(total_price):
        return total_price

    @staticmethod
    def regular_customer_discount(total_price):
        return total_price - (total_price * Discount.REGULAR_CUSTOMER)

    @staticmethod
    def holiday_special_discount(total_price):
        if total_price > 100:
            return total_price - Discount.HOLIDAY_SPECIAL
        return total_price