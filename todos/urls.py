from django.contrib import admin
from django.urls import path, include
from addTodo import urls as addTodo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(addTodo_urls, namespace='addTodo')),
]
