from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from logs.models import ActivityLog


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()

    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        task = serializer.save(
            created_by=self.request.user
        )

        ActivityLog.objects.create(
            user=self.request.user,
            action="TASK_CREATED",
            entity_type="TASK",
            entity_id=task.id
        )

    def get_queryset(self):

        user = self.request.user

        if user.role == "ADMIN":
            return Task.objects.all()

        elif user.role == "TEAM_LEAD":
            return Task.objects.filter(
                assigned_to__team=user.team
            )

        elif user.role == "FIELD_AGENT":
            return Task.objects.filter(
                assigned_to=user
            )

        elif user.role == "AUDITOR":
            return Task.objects.all()

        return Task.objects.none()