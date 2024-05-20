from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentFilter(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        type_product = self.request.query_params.get('type_product')
        product_id = self.request.query_params.get('product_id')
        return Comment.objects.filter(type_product=type_product, product_id=product_id)
