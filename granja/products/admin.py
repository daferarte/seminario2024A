from django.contrib import admin
from .models import categories
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('name', 'description')
    list_display = ('name', 'create_at', 'update_at')
    ordering = ('create_at',)


admin.site.register(categories, CategoryAdmin)