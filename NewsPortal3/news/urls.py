from django.urls import path
from .views import PostsList, PostsDetail  # импортируем наше представление

urlpatterns = [
    path('', PostsList.as_view()), # нужно представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostsDetail.as_view()),  # pk — это первичный ключ товара
]