from django.urls import path
from .views import RefbookView, RefbookElementView, CheckRefbookElementView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('reefbooks/', RefbookView.as_view()),
    path('reefbooks/<id>/elements', RefbookElementView.as_view()),
    path('reefbooks/<id>/check_element', CheckRefbookElementView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
