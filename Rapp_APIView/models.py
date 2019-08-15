from django.db import models
# Create your models here.
class Product (models.Model):
    p_id = models.IntegerField(primary_key=1)
    p_name = models.CharField(max_length=30)
    p_cost = models.DecimalField(max_digits=10, decimal_places=2)
    p_mfd = models.DateField()
    p_exd = models.DateField()
