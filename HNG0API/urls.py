from django.urls import path
from .views import hng0_api

urlpatterns = [
    path('', hng0_api, name='hng0_api')
]

