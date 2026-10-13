from django.db import models

# Create your models here.
class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_delivered = models.BooleanField(default=False)

    def _str_(self):
        return self.customer_name