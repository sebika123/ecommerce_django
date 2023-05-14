from django.db import models

# Create your models here.
class Products(models.Model):

    type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products')
    discount = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    details = models.TextField(null=True, blank=True)
    #features = models.TextField(null=True, blank=True)
    #specification = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Products'