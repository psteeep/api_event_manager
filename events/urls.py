from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EventViewSet, UserRegistrationView, EventRegistrationCreateAPIView, EventRegistrationListAPIView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registrations/', EventRegistrationCreateAPIView.as_view(), name='event-registration-create'),
    path('registrations/my/', EventRegistrationListAPIView.as_view(), name='event-registration-list'),
]
