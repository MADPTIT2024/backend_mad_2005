from django.db import models

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=100)	

    def __str__(self):
        return self.name

class Types(models.Model):
    name = models.CharField(max_length=100)	

    def __str__(self):
        return self.name


class Mobile(models.Model):
    title = models.CharField(max_length=100)	
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.CharField(max_length=500,null=True)

    is_sale = models.BooleanField(default=False,null=True)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6,null=True)

    def __str__(self):
        return self.title
