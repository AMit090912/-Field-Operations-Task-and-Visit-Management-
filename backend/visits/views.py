from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Visit
from .serializers import VisitSerializer
from logs.models import ActivityLog
from ai_service.services import MockAIService


class VisitViewSet(viewsets.ModelViewSet):

    queryset = Visit.objects.all()

    serializer_class = VisitSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        notes = self.request.data.get("notes", "")

        ai_result = MockAIService.analyze_notes(notes)

        visit = serializer.save(
            agent=self.request.user,
            ai_summary=ai_result["summary"],
            risk_flag=ai_result["risk"]
        )
        ActivityLog.objects.create(
            user=self.request.user,
            action="VISIT_CREATED",
            entity_type="VISIT",
            entity_id=visit.id
        )

    def get_queryset(self):

        user = self.request.user

        if user.role == "ADMIN":
            return Visit.objects.all()

        elif user.role == "FIELD_AGENT":
            return Visit.objects.filter(agent=user)

        return Visit.objects.all()