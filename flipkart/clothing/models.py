from django.db import models

# Create your models here.
class Product(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
    ]
    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Pink', 'Pink'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Yellow', 'yellow'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Beige','Beige'),
    ]

    name = models.CharField(max_length = 200)
    size = models.CharField(max_length = 4, choices = SIZE_CHOICES, default = 'S')
    color = models.CharField(max_length = 10, choices = COLOR_CHOICES, default = 'RED')
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    image = models.ImageField(upload_to='product_img/')

    def __str__(self):
        return self.name