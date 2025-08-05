from django.contrib import admin
from .models import BlogPost, Category, BlogSection, ListItems
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class ListItemsInline(NestedTabularInline):
    model = ListItems
    extra = 1
    fields = ['item']

class BlogSectionInline(NestedStackedInline):
    model = BlogSection
    extra = 1
    fields = ['image', 'heading', 'content', 'order']
    inlines = [ListItemsInline]

@admin.register(BlogSection)
class BlogSectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'image', 'content', 'order']

@admin.register(BlogPost)
class BlogPostAdmin(NestedModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BlogSectionInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


