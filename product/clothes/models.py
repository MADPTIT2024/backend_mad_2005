from django.db import models

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=100)	

    def __str__(self):
        return self.name

class Styles(models.Model):
    name = models.CharField(max_length=100)	

    def __str__(self):
        return self.name


class Cloth(models.Model):
    title = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)	
    styles = models.ForeignKey(Styles, on_delete=models.CASCADE, null=True)	
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/',null=True)

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.title