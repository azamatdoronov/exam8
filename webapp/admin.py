from django.contrib import admin


from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'image', 'created_time', 'updated_time']
    list_display_links = ['description']
    list_filter = ['name', 'category']
    search_fields = ['category']
    fields = ['name', 'description', 'category', 'image', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
