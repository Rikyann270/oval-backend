from django.urls import path

from chicken.api.views import (
    api_chick_detail_view,
    api_equipments_detail_view,
    api_feeds_detail_view,
    ApiChickListView,
    ApiEquipmentsListView,
    ApiFeedsListView,
    )

app_name = 'chicken'

urlpatterns = [
    path('chick/<slug>/', api_chick_detail_view, name="detail"),
    path('equipments/<slug>/', api_equipments_detail_view, name="detail"),
    path('feeds/<slug>/', api_feeds_detail_view, name="detail"),


    path('chick/list', ApiChickListView.as_view(), name="list"),
    path('equipments/list', ApiEquipmentsListView.as_view(), name="list2"),
    path('feeds/list', ApiFeedsListView.as_view(), name="list"),


]