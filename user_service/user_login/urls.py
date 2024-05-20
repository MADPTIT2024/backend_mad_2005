from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView

router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'login', LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]
