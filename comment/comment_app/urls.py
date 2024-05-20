from django.urls import path
from .views import CommentListCreate, CommentFilter

urlpatterns = [
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/filter/', CommentFilter.as_view(), name='comment-filter'),
]
