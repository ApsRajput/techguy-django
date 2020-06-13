from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Techguy(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(default='',max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    email = models.CharField(max_length=40, null=True)
    category = models.ManyToManyField('Category', related_name='posts', blank=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Techguy, self).save(*args, **kwargs)

class Customer(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPE = (
        ("Physical", "Physical"),
        ("Downloadable", "Downloadable")
    )
    name = models.CharField(max_length=20)
    sku = models.CharField(max_length=10)
    quantity = models.IntegerField()
    product_type = models.CharField(choices=PRODUCT_TYPE, default="Physical", max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = (
        ("Pending", "Pending"),
        ("Dispatched", "Dispatched"),
        ("Delivered", "Delivered")
    )
    order_id = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS, max_length=50)

    class Meta:
        verbose_name =  ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return self.order_id

    # def get_absolute_url(self):
    #     return reverse("Order_detail", kwargs={"pk": self.pk})
