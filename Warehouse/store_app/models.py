from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store')
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    inventory_quantity = models.PositiveSmallIntegerField()
    inventory_updated_time = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

