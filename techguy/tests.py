from django.test import TestCase

# Create your tests here.
class TestModels(TestCase):
    def customer_has_a_product_order(self):
        order = Order.objects.create(order_id="", status="Delivered")
        customer = Customer.objects.create(name="Aps Rajput")
        product = Customer.objects.create(name="product 1", sku="12dq", quantity="2", product_type="Downloadable")
        book.authors.set([philip.pk, juliana.pk])
        self.assertEqual(book.authors.count(), 2)