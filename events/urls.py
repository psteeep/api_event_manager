from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView, EventUpdateAPIView, EventDeleteAPIView, AllEventsAPIView

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('events/all/', AllEventsAPIView.as_view(), name='all-events'),
    path('events/<int:pk>/update/', EventUpdateAPIView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDeleteAPIView.as_view(), name='event-delete'),
]
