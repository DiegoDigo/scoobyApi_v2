from __future__ import unicode_literals
from django.db import models


class ProductQuerySet(models.query.QuerySet):

    def products(self):
        return self.all()

    def product_by_id(self, id_product: int):
        return self.filter(pk=id_product)