app_name = 'apis'

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GymViewSet, TrainerViewSet, ClientViewSet, WorkoutSessionViewSet

# Create a router and register the viewsets with it.
router = DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gym')
router.register(r'trainers', TrainerViewSet, basename='trainer')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'workouts', WorkoutSessionViewSet, basename='workout')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
