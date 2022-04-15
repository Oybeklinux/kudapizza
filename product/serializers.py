from rest_framework import serializers
from .models import *


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

    def to_representation(self, obj):
        # url = None
        # if obj.image and hasattr(obj.image, 'url'):
        #     url = obj.image.url
        #     request = self.context.get('request', None)
        #     if request is not None:
        #         url = request.build_absolute_uri(url)
        
        return {
            "id": obj.id,
            "name_uz": obj.name_uz,
            "name_en": obj.name_en,
            "name_ru": obj.name_ru,
            "definition_uz": obj.definition_uz,
            "definition_en": obj.definition_en,
            "definition_ru": obj.definition_ru,
            "image": obj.image,#obj.url
            "price": obj.price,
            "count": 1,
            "created": obj.created,
            "category": {
                "name_uz": obj.category.name_uz,
                "name_en": obj.category.name_en,
                "name_ru": obj.category.name_ru,
                "id": obj.category.id
            } if obj.category else None
        }


class CategorySerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, obj):

        return {
            "id": obj.id,
            "total": obj.total,
            "phone": obj.phone,
            "address": obj.address,
            "created": obj.created,
            "pizza": {
                "name_uz": obj.bottle.name_uz,
                "name_en": obj.bottle.name_en,
                "name_ru": obj.bottle.name_ru,
                "definition_uz": obj.definition_uz,
                "definition_en": obj.definition_en,
                "definition_ru": obj.definition_ru,
                "id": obj.bottle.id
             }
        }
