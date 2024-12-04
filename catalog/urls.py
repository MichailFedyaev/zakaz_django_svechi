from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [
    path('list/', views.CandleListView.as_view(), name="candles_list"),
    path("candle/create", views.CandleCreateView.as_view(), name="candle_create"),
    path("candle/<int:pk>", views.CandleDetailView.as_view(), name="candle_detail"),
]