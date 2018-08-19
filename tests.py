import os
import unittest
from decimal import Decimal
from datetime import datetime, timedelta

from models.user import User, UserGroup
from models.cart import Cart, CartItem
from models.product import Product
from models.offer import Offer


class CartTest(unittest.TestCase):

    def _create_user(self):
        user = User('John Doe 1', 'john.doe@example.com', UserGroup.GOLD)
        return user

    def _create_cart(self):
        iphone_silver = Product('Iphone Silver', 'Silver', 999)
        iphone_black = Product('Iphone Black', 'Black', 899)
        cart = Cart(self._create_user())
        cart.add(iphone_silver, 2)
        cart.add(iphone_black, 1)

        return cart


    def test_get_total_(self):
        cart = self._create_cart()
        total = cart.get_total()
        self.assertEqual(total, Decimal('2897'))


    def test_get_total_offer(self):
        cart = self._create_cart()
        offer = Offer(UserGroup.GOLD, datetime.now(), datetime.now() + timedelta(days=1), 'black', 1500, 50)
        total = cart.get_total(offer)
        self.assertEqual(total, Decimal('2847'))

    def test_get_total_offer_2(self):
        cart = self._create_cart()
        offer = Offer(UserGroup.GOLD, datetime.now(), datetime.now() + timedelta(days=1), 'black', 3000, 50)
        total = cart.get_total(offer)
        self.assertEqual(total, Decimal('2847'))
