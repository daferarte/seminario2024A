from django.contrib import admin
from .models import categories, products
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('name', 'description')
    list_display = ('name', 'create_at', 'update_at')
    ordering = ('create_at',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at', 'user')
    search_fields = ('name', 'description', 'cost', 'user__username', 'categorie__name')
    list_filter = ('public', 'expiryDate', 'expiryTime', 'categorie')
    list_display = ('name', 'public', 'expiryDate', 'expiryTime', 'create_at', 'update_at')
    ordering = ('-create_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


admin.site.register(categories, CategoryAdmin)
admin.site.register(products, ProductAdmin)
