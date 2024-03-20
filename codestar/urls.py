from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("about/", include("about.urls")),  # Prefixed with about/
    path("", include("blog.urls")),  # Prefixed with blog/
    path('summernote/', include('django_summernote.urls')),
]
