from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('',views.index_unlog,name='index_unlog'),
    path('login',views.login,name='login'),
    path('log',views.logsuccess,name='login-success'),
    path('register',views.register,name='register'),
    path('forget',views.forget_password,name='forget'),
    path('reset',views.reset,name='reset'),
    path('summernote/', include('django_summernote.urls')),
    path('logout',views.log_out,name='logout'),
]

