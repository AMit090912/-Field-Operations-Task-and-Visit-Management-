from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from tasks.models import Task
from visits.models import Visit


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_summary(request):

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status="COMPLETED"
    ).count()

    total_visits = Visit.objects.count()

    return Response({
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "total_visits": total_visits,
    })