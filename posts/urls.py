from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('new_post/', views.NewPost, name='newpost'),
    path('<int:pk>/', views.PostDetail, name='postdetail'),
    path('<int:pk>/delete/', views.DeletePost, name='deletepost'),
    path('<int:pk>/edit/', views.EditPost, name='editpost'),
]
