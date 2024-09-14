from django.urls import path
from .views import BusinesProfileDetailView, BusinessProfileListCreateView

urlpatterns = [
    path('', BusinessProfileListCreateView.as_view(), name='business-profile-list-create'),
    path('<int:pk>/', BusinesProfileDetailView.as_view(), name='business-profile-detail'),
]