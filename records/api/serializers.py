from rest_framework import serializers

from records.models import(
    Record,
)

class RecordSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Record
        # fields = ['name', 'price','Image']
        fields = ['title', 'item_name', "total_price", 'date_published', 'quantity' , "date"]

class RecordCkSerializer(serializers.ModelSerializer):

    # inital_price = serializer.IntegerField(null=False, blank=False)

    class Meta:
        model = Record
        # fields = ['name', 'price','Image']
        fields = ['title', 'item_name', 'inital_price', 'quantity', "date", "total_price"]
