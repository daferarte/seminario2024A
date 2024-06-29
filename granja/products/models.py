from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(default='null', blank=True, null=True, verbose_name="Foto", upload_to="categories")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return str(self.name)
    
class products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    cost = models.FloatField(verbose_name='Precio producto')
    quantity = models.IntegerField(verbose_name='Cantidad de producto')
    image = models.ImageField(default='null', blank=True, null=True, verbose_name="Foto", upload_to="categories")
    datePacked = models.DateField(auto_now=False, verbose_name="Fecha de empaquetado")
    expiryDate = models.DateField(auto_now=False, verbose_name="Fecha de vencimiento")
    expiryTime = models.TimeField(auto_now=False, verbose_name="Hora de expiración")
    public = models.BooleanField(default=False, verbose_name="¿Publicado?")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.PROTECT, blank=True, null=True)
    categorie = models.ManyToManyField(categories, blank=True, verbose_name="Categorías")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-create_at']
        
    def __str__(self):
        return str(self.name)