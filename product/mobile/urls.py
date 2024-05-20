from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProducerViewSet,TypesViewSet, MobileViewSet

router = DefaultRouter()
router.register(r'types', TypesViewSet)
router.register(r'producers', ProducerViewSet)
router.register(r'mobiles', MobileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]