from django.contrib.auth.models import User
from django.db import models

from product.models import Product

class List(models.Model):
    user = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.id

class ListItem(models.Model):
    list = models.ForeignKey(List, related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
