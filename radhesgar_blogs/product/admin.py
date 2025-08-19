from django.contrib import admin
from product.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ('image', )


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1
    fields = ('feature', )


class ProductApplicationInline(admin.TabularInline):
    model = ProductApplication
    extra = 1
    fields = ('application', )


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1
    fields = ('key', 'value')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name",)}
    list_display = ('product_name', 'slug')
    inlines = [ProductImageInline, ProductFeatureInline, ProductApplicationInline, ProductSpecificationInline]

@admin.register(CalibrationSoftware)
class CalibrationSoftwareAdmin(admin.ModelAdmin):
    list_display = ('software_name', 'software_version')

@admin.register(ModbusSoftware)
class ModbusSoftwareAdmin(admin.ModelAdmin):
    list_display = ('software_name', 'software_version')

