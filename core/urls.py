from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.yasg import urlpatterns as yasg
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.views.static import serve as static_serve


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        TemplateView.as_view(template_name="index.html"),
        name="frontend",
    ),

    re_path(
        r"^assets/(?P<path>.*)$",
        static_serve,
        {"document_root": settings.BASE_DIR / "dist" / "assets"},
        name="frontend-assets",
    ),
    path("api/laiding/", include("app.laiding.urls")),

    path("", include(yasg)),
]

urlpatterns += i18n_patterns(
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
