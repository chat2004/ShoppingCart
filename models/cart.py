from decimal import Decimal


class Cart(object):
    def __init__(self, user):
        self.user = user
        self.items = []

    def __len__(self):
        return len(self.items)

    def get_total(self, offer=None):
        totals = []
        for item in self.items:
            line_total = item.get_line_total()

            totals.append(line_total)

        cart_total = Decimal(sum(totals))

        # Check discount rule
        is_offer = True
        if offer is not None:
            if is_offer and cart_total < offer.sub_total:
                is_offer = False
            if is_offer and self.user.group != offer.group:
                is_offer = False
            color_found = next((item for item in self.items if item.product.color.lower() == offer.color.lower()), None)
            if color_found is None:
                is_offer = False

            if is_offer:
                cart_total -= offer.discount

        return cart_total

    def add(self, item, quantity=1):
        cart_item = self.get_item(item)
        if cart_item is None:
            cart_item = CartItem(item, quantity)
            self.items.append(cart_item)
        else:
            cart_item.quantity += quantity
        return cart_item

    def get_item(self, item_name):
        return next((item for item in self.items if item.product == item_name), None)


class CartItem(object):

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_line_total(self):
        return self.product.price * self.quantity
