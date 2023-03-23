from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import ProductSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class RatingViewSet(ModelViewSet):
    # queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Rating.objects.filter(product_id = self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        user_id = self.request.user.id
        product_id = self.kwargs["product_pk"]
        return {"user_id": user_id, "product_id": product_id}