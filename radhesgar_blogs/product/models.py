from django.db import models
from django.utils.text import slugify


class CalibrationSoftware(models.Model):
    software_name = models.CharField(max_length=255, null=True, blank=True)
    software_version = models.CharField(max_length=255, null=True, blank=True)
    software_file = models.FileField(upload_to='./downloads')
    software_version = models.CharField(max_length=255, default="latest")
    objects = models.Manager()

    def __str__(self):
        return f'{self.software_name} - {self.software_version}'

class ModbusSoftware(models.Model):
    software_name = models.CharField(max_length=255, null=True, blank=True)
    software_file = models.FileField(upload_to='./downloads')
    software_version = models.CharField(max_length=255, default="latest")
    objects = models.Manager()

    def __str__(self):
        return f'{self.software_name} - {self.software_version}'


class Product(models.Model):
    page_title = models.CharField(max_length=250, blank=True)
    sub_title = models.CharField(max_length=300, blank=True)
    product_name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    datasheet = models.FileField(upload_to='./downloads', blank=True, null=True)
    calibration_software = models.ForeignKey(CalibrationSoftware, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    modbus_software = models.ForeignKey(ModbusSoftware, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_features')
    feature = models.CharField(max_length=250)

    def __str__(self):
        return self.feature


class ProductApplication(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_applications')
    application = models.CharField(max_length=250)

    def __str__(self):
        return self.application


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_specifications')
    key = models.CharField(max_length=250)
    value = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.key}: {self.value}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='./product_images')
    objects = models.Manager()

    def __str__(self):
        return self.image.name if self.image else "No image"


