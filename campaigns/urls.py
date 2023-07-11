from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DonationViewSet, UserCreate, CustomAuthToken

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('api-auth/', include('rest_framework.urls')),
]
