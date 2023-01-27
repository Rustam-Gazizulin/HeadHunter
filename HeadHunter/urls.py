from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from HeadHunter import settings
from vacancies import views
from vacancies.views import SkillsViewSet

router = routers.SimpleRouter()
router.register('skill', SkillsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('hello/', views.hello),
    path('vacancy/', include('vacancies.urls')),
    path('company/', include('companies.urls')),
    path('user/', include('authentication.urls')),
]


urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

