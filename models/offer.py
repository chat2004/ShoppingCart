from datetime import datetime
from decimal import Decimal

class Offer(object):

    def __init__(self, group, from_date, to_date, color, sub_total, discount):
        self.group = group
        self.from_date = from_date
        self.to_date = to_date
        self.color = color
        self.sub_total = sub_total
        self.discount = discount

    # def calculate_line_total(self, cart_item):
    #     current_date = datetime.now()
    #     line_total = cart_item.product.price * cart_item.quantity
    #     if current_date >= self.from_date and current_date <= self.to_date:
    #         if cart_item.product.color.lower() == self.color.lower() and line_total >= self.sub_total:
    #             line_total -= self.discount
    #
    #     return line_total
