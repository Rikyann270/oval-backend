from rest_framework import serializers
from chicken.models import (
    ChickInfor,
    EquipmentsInfor,
    FeedsInfor,
    VaccineInfor,

    )

class ChickInforSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChickInfor
        # fields = ['name', 'price','Image']
        fields = ['name', 'moreInfo', 'price', 'dates', 'Image']



class EquipmentsInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentsInfor
        fields = ['name', 'price','Image','slug']


class FeedsInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedsInfor
        fields = ['name', 'price','Image','slug']


