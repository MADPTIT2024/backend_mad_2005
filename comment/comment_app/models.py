from django.db import models

class Comment(models.Model):
    star = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    user = models.CharField(max_length=100,null=True)
    product_id = models.IntegerField(null=True)
    type_product = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.user} - {self.type_product}'
