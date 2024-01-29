from rest_framework import serializers

from mvideo.models import NetworkUnit


class NetworkUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkUnit
        fields = '__all__'


class NetworkUnitUpdateSerializer(serializers.ModelSerializer):

    """Обновление объекта"""

    class Meta:
        model = NetworkUnit

        # Исключаем возможность обновления задолженности через API

        exclude = ['debt_to_supplier']

