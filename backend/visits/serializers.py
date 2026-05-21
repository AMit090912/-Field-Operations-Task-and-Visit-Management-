from rest_framework import serializers
from .models import Visit


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = "__all__"

        read_only_fields = (
            "agent",
            "ai_summary",
            "risk_flag",
            "started_at",
            "completed_at",
        )