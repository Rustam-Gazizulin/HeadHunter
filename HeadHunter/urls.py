from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from HeadHunter import settings
from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('vacancy/', include('vacancies.urls')),
    path('company/', include('companies.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

