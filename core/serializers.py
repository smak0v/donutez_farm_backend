from rest_framework import serializers

from core.models import Token, YF


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        exclude = (
            'created_at',
            'updated_at',
        )


class YFSerializer(serializers.ModelSerializer):
    class Meta:
        model = YF
        exclude = (
            'created_at',
            'updated_at',
        )
