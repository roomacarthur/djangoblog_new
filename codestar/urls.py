from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),  # Prefixed with blog/
    path("about/", include("about.urls")),  # Prefixed with about/
    path('summernote/', include('django_summernote.urls')),
]
