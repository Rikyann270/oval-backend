from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


from records.models import (
    Record,

    )

from records.api.serializers import (
    RecordSerializer,
    RecordCkSerializer,


    )

@api_view(['GET', ])
def api_record_detail_view(request, slug):
    try:
        record_info=Record.objects.get(slug=slug)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = RecordSerializer(record_info)
        return Response(serializer.data)


@api_view(['POST', ])
def api_create_record_view(request):
    account = request.user
    print(request.user)
    if not request.user.is_authenticated:
        # You might want to return a response indicating that the user is not authenticated
        return Response({"error": "User not logged in"}, status=401)


    record_info = Record(author=account)


    if request.method=="POST":
        serializer = RecordCkSerializer(record_info, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ApiRecordsListView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = PageNumberPagination




