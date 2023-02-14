from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from todo_api.models import Todo, Image
from todo_api.serializers import TodoListSerializer, TodoCreateSerializer, ImageSerializer, TodoDetailSerializer, \
    CheckStatusSerializer
from todo_api.permissions import IsAuthorOrReadOnly, IsAuthorOrAssignee
from rest_framework.parsers import MultiPartParser, FormParser


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]


class CheckStatusView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = CheckStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrAssignee]


class UploadImageView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))
