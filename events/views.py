from rest_framework import generics, viewsets, status
from .models import Event, EventRegistration
from django.contrib.auth.models import User
from .serializers import EventSerializer, UserRegistrationSerializer, EventRegistrationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'location', 'date']
    search_fields = ['title', 'description']
    ordering_fields = ['date', 'title']

    @action(detail=False, methods=['get'])
    def all(self, request):
        events = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def register(self, request, pk=None):
        event = self.get_object()
        user = request.user
        if EventRegistration.objects.filter(user=user, event=event).exists():
            return Response({'detail': 'You are already registered for this event.'}, status=400)

        registration = EventRegistration.objects.create(user=user, event=event)
        serializer = EventRegistrationSerializer(registration)
        return Response(serializer.data, status=201)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class EventRegistrationCreateAPIView(generics.CreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id  # Automatically set the user from the request
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventRegistrationListAPIView(generics.ListAPIView):
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EventRegistration.objects.filter(user=self.request.user)
