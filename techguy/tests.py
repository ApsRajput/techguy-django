from django.test import TestCase
from .models import *

# Create your tests here.
# class TestModels(TestCase):
#     def customer_has_a_product_order(self):
#         order = Order.objects.create(order_id="", status="Delivered")
#         customer = Customer.objects.create(name="Aps Rajput")
#         product = Customer.objects.create(name="product 1", sku="12dq", quantity="2", product_type="Downloadable")
#         book.authors.set([philip.pk, juliana.pk])
#         self.assertEqual(book.authors.count(), 2)

class ProductTestCases(TestCase):
    def setup(self):
        return Product.objects.create(name="Samsung A6", sku="12ew", quantity=2, product_type="Downloadable")
        # Product.objects.create(name="PubG", sku="33ew", quantity=2, product_type="Physical")

    def create_model_test(self):
        product = self.setup()
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__self__(), product.title)
