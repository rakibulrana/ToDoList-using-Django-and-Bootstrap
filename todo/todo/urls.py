
from django.contrib import admin
from django.urls import path


from todoapp.views import HomePage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage)
]
