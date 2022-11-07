from django.urls.conf import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"submissions",
    views.SubmissionViewSet,
)

urlpatterns = [
    path(
        "",
        include(router.urls),
    ),
    path(
        "knapsack",
        views.KnapsackView.as_view(),
        name="knapsack",
    ),
]
