from django.urls import path
from todo_api.views import TodoListView, TodoCreateView, TodoUpdateDeleteView, UploadImageView, CheckStatusView

urlpatterns = [
    path('todos', TodoListView.as_view()),
    path('todos/add', TodoCreateView.as_view()),
    path('todos/<int:pk>', TodoUpdateDeleteView.as_view()),
    path('check_status/<int:pk>', CheckStatusView.as_view()),
    path('upload_image', UploadImageView.as_view()),
]
