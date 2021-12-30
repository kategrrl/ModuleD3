from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')), # делаем так, чтобы все адреса из news сами автомат.
    # подключались когда мы их добавим
]
