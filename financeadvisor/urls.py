from django.contrib import admin
from django.urls import path, include
from advisor.views import home  # <-- import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),   # <-- this handles http://127.0.0.1:8000/
   path('api/', include('advisor.urls')),
]
