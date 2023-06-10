from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action == 'list':
            # only admin can see all tasks
            permission_classes = [permissions.IsAdminUser]
        else:
            # only owner can see or edit their own task
            permission_classes = [permissions.IsAuthenticated, permissions.IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # set the owner as the current user
        serializer.save(owner=self.request.user)