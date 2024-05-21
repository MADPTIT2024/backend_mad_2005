from django.urls import path
from .views import (
    StylesListCreate,
    StylesRetrieveUpdateDestroy,
    ProducerListCreate,
    ProducerRetrieveUpdateDestroy,
    ClothListCreate,
    ClothRetrieveUpdateDestroy,
)

urlpatterns = [
    path("styles/", StylesListCreate.as_view(), name="styles-list"),
    path(
        "styles/<int:pk>/", StylesRetrieveUpdateDestroy.as_view(), name="styles-detail"
    ),
    path("producers/", ProducerListCreate.as_view(), name="producer-list"),
    path(
        "producers/<int:pk>/",
        ProducerRetrieveUpdateDestroy.as_view(),
        name="producer-detail",
    ),
    path("cloths/", ClothListCreate.as_view(), name="cloth-list"),
    path("cloths/<int:pk>/", ClothRetrieveUpdateDestroy.as_view(), name="cloth-detail"),
]
