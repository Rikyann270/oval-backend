from django.urls import path

from records.api.views import (
    api_record_detail_view,
    api_create_record_view,

    ApiRecordsListView

    )

app_name = 'records'

urlpatterns = [
    path('<slug>/', api_record_detail_view, name="detail"),
    path('create', api_create_record_view, name="create"),



    path('record/list', ApiRecordsListView.as_view(), name="list"),



]