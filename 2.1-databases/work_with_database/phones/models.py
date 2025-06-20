from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='products')
    release_date = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField(null=True, blank=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True)


    def __str__(self):
        return self.name
