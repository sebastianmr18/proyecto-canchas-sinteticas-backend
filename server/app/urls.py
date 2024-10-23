from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import UserViewSet, CourtViewSet, ReservationViewSet, PaymentViewSet, ReviewViewSet
from .views.user_view import UserRegistrationView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courts', CourtViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
