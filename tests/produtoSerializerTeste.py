from django.test import TestCase
from product.api.serializers import ProductSerialzier, CreateProductSerializer
from product.models import Product


class TestArquivoSerializer(TestCase):

    def setUp(self):
        self.data = {
            "type_product": {
                "id": 1,
                "categoy": "teste9",
                "slug_category": "Teste9"
            },
            "name": "teste api  2",
            "description": "Teste Api 2",
            "price": "10.00",
            "stock": 10,
            "image": None
        }

    def test_not_create_product(self):
        serializer = CreateProductSerializer(data={})
        self.assertFalse(serializer.is_valid())
