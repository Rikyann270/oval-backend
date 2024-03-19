from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


from chicken.models import (
    ChickInfor,
    EquipmentsInfor,
    FeedsInfor,

    )

from chicken.api.serializers import (
    ChickInforSerializer,
    EquipmentsInforSerializer,
    FeedsInforSerializer,

    )

@api_view(['GET', ])
def api_chick_detail_view(request, slug):
    try:
        chick_info=ChickInfor.objects.get(slug=slug)
    except ChickInfor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = ChickInforSerializer(chick_info)
        return Response(serializer.data)

@api_view(['GET', ])
def api_equipments_detail_view(request, slug):
    try:
        equipments_info=EquipmentsInfor.objects.get(slug=slug)
    except EquipmentsInfor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = EquipmentsInforSerializer(equipments_info)
        return Response(serializer.data)

@api_view(['GET', ])
def api_feeds_detail_view(request, slug):
    try:
        feeds_info=FeedsInfor.objects.get(slug=slug)
    except FeedsInfor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = FeedsInforSerializer(feeds_info)
        return Response(serializer.data)






class ApiChickListView(ListAPIView):
    queryset = ChickInfor.objects.all()
    serializer_class = ChickInforSerializer
    pagination_class = PageNumberPagination

class ApiEquipmentsListView(ListAPIView):
    queryset = EquipmentsInfor.objects.all()
    serializer_class = EquipmentsInforSerializer
    pagination_class = PageNumberPagination

class ApiFeedsListView(ListAPIView):
    queryset = FeedsInfor.objects.all()
    serializer_class = FeedsInforSerializer
    pagination_class = PageNumberPagination

