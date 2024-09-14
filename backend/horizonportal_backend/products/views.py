from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Product 
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Product.objects.all()

    def perform_create(self, serializer):
        business = self.request.user.businessprofile
        serializer.save(business=business)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.businessprofile == self.get_object().business:
            serializer.save()
        else:
            raise PermissionDenied("You do not have the permission to edit this business profiles.")
