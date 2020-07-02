from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
from django.utils import timezone


class Product(models.Model):
    # contain Product's information
    Condition_Type = (
        ("New", "New"),
        ("Used", "USed")
    )
    Name = models.CharField(max_length=100)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Description = models.TextField(max_length=500)
    Condition = models.CharField(max_length=100, choices=Condition_Type)
    Price = models.DecimalField(max_digits=7 , decimal_places=0)
    image = models.ImageField(upload_to='main_products/', blank=True, null=True)
    Created = models.DateTimeField(default=timezone.now)
    Category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    Brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.Name:
            self.slug = slugify(self.Name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.Name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.Name


class Category(models.Model):
    # For Item/product Category
    Category_Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='category/', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.Category_Name:
            self.slug = slugify(self.Category_Name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.Category_Name


class Brand(models.Model):
    # For Item/product brand
    Brand_Name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.Brand_Name
