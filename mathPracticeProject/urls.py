from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', views.auth, name='auth'),
    path('index/', include("app.urls")),
    path('', views.auth),
    path('practice_detail/', views.practice_detail, name='practice_detail'),
    path('exam_detail/', views.exam_detail, name='exam_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)