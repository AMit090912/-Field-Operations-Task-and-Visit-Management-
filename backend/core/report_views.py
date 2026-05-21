from datetime import timedelta

from django.db.models import Count
from django.utils.timezone import now

from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.models import Task
from visits.models import Visit


@api_view(["GET"])
def pending_tasks_by_region(request):

    data = (
        Task.objects
        .filter(status="PENDING")
        .values("region")
        .annotate(total=Count("id"))
    )

    return Response(data)


@api_view(["GET"])
def recent_visits(request):

    last_week = now() - timedelta(days=7)

    visits = Visit.objects.filter(
        started_at__gte=last_week
    ).count()

    return Response({
        "visits_last_7_days": visits
    })


@api_view(["GET"])
def task_status_distribution(request):

    data = (
        Task.objects
        .values("status")
        .annotate(total=Count("id"))
    )

    return Response(data)