from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', include('companies.urls')),
    path('users/', include('users.urls')),
    path('documents/', include('documents.urls'))
]

if settings.DEBUG is False:
    urlpatterns += [
        path("health/", lambda r: HttpResponse("OK"), name="health"),
    ]
