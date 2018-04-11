from cloudinary.models import CloudinaryField
from django.db import models
from product.querys import ProductQuerySet


class TypeProduct(models.Model):
    category = models.CharField("Categoria", max_length=50, unique=True)
    slug_category = models.SlugField(verbose_name="link unico", null=True, blank=True)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug_category = self.category
        super(TypeProduct, self).save(*args, **kwargs)

    class Meta:
        ordering = ['category', ]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    name = models.CharField('nome', max_length=50)
    description = models.TextField('descricao')
    price = models.DecimalField('preço', max_digits=10, decimal_places=2)
    stock = models.IntegerField('estoque')
    image = CloudinaryField('image', null=True, blank=True)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, verbose_name="tipo de produto")
    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'stock', 'price']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'