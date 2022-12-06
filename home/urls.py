from django.urls import path
from home import  views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register_view'),
    path('add-blog/', views.add_blog, name="add_blog"),
    path('blog-detail/<str:slug>/', views.blog_detail, name="blog_detail"),
    path('see-blog/', views.see_blog, name="see_blog"),
    path('blog-delete/<str:slug>/', views.blog_delete, name="blog_delete"),
    path('blog-update/<str:slug>/', views.blog_update, name="blog_update"),
    path('logout-view/', views.logout_user, name="logout"),

]


