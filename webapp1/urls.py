from django.urls import path
from .views import postlistview , postdetailview , postcreateview , postupdateview , postdeleteview , userpostlistview
from webapp1 import views


urlpatterns = [
    path('', postlistview.as_view() , name='app_home'),
    path('user/<str:username>', userpostlistview.as_view() , name='user_posts'),
    path('post/<int:pk>/', postdetailview.as_view() , name='post_detail'),
    path('post/<int:pk>/update/', postupdateview.as_view() , name='post_update'),
    path('post/<int:pk>/delete/', postdeleteview.as_view() , name='post_delete'),
    path('post/new/', postcreateview.as_view() , name='post_create'),
    path('about/', views.about , name='app_about'),
]
