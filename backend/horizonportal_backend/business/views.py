from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import BusinessProfile
from .serializers import BusinessProfileSerializer

class BusinessProfileListCreateView(generics.ListCreateView):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class BusinesProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user == self.get_object().owner:
            serializer.save()
        else:
            raise PermissionDenied("You do not have the permission to edit this business profiles.")

