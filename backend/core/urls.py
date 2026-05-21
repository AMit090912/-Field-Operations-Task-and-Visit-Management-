from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .dashboard_views import dashboard_summary
from .frontend_views import home
from .report_views import (
    pending_tasks_by_region,
    recent_visits,
    task_status_distribution,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
       path("", lambda request: HttpResponse("Backend Running")),

    path("api/", include("tasks.urls")),

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include("visits.urls")),
    path("api/", include("logs.urls")),
    path("api/dashboard/", dashboard_summary),
    path("api/reports/pending-tasks/",pending_tasks_by_region),

    path("api/reports/recent-visits/",recent_visits),

    path("api/reports/task-status/",task_status_distribution),
        
]