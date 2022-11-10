
from django.contrib import admin
from django.urls import path


from todoapp.views import HomePage, Edittodo, Updatetodo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage),
    path('delete-<int:id>/', Edittodo),
    path("update-<int:id>/", Updatetodo)
]
