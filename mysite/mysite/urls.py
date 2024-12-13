# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_app.urls')),  # This includes all URLs from crud_app
    path('accounts/', include('accounts.urls')),
]
