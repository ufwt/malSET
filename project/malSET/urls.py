from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('report/<str:filename_b64>/', views.report, name="report"),

    path('upload/', views.file_upload, name="upload"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)