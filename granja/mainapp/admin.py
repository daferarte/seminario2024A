from django.contrib import admin
from .models import Persons, TipeDocument
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'create_at', 'update_at')
    search_fields = ('typeDocument', 'cedula', 'user__username', 'birthDay')
    list_filter = ('public',)
    list_display = ('cedula', 'public', 'create_at', 'user')
    ordering = ('-create_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


class TypeDocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('name', 'Persons__cedula', 'birthDay')
    list_display = ('name', 'create_at', 'update_at')
    ordering = ('-create_at',)


admin.site.register(Persons, PersonAdmin)
admin.site.register(TipeDocument, TypeDocumentAdmin)