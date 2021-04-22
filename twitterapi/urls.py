from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


TwitterBaserouter = DefaultRouter()

TwitterBaserouter.register(r"twitter/tweets", views.TwitterViewSet, basename="twitter-tweets")