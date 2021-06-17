from django.urls import path
from blog import views
app_name = 'blog'
urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:id>', views.category, name='category'),
    path('tags/', views.tags, name='tags'),
    path('tags/<int:id>/', views.tag_detail, name='tags_detail'),
    path('articles/<int:id>/', views.detail, name='detail'),
    path('commentpost',views.commentpost,name='commentpost'),
    path('userinfo',views.user_info,name='userinfo'),
    path('info/<comment_id>',views.comment_del,name="comm_del"),
    path('commentdel',views.comment_del,name='comment_del'),
    path('search/',views.search,name='search'),
]