from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/update/<int:post_id>/', views.update_post, name='update_post'),  # Update operation
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Delete operation
]

