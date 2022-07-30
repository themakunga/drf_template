from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter(trailing_slash=False)
router.register(r'', views.UsersViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
