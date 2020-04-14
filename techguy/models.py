from django.db import models

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
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    email = models.CharField(max_length=40, null=True)
    category = models.ManyToManyField('Category', related_name='posts', null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

