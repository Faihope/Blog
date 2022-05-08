from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('<int:pk>',views.postDetail,name='postDetail'),
    path('about',views.About,name='About'),
    path('contact',views.Contact,name='Contact'),
    path('newpost',views.newPosts,name='newPosts'),
    path('register/',views.registeruser,name='registeruser'),
    path('loginuser/', views.loginpage, name="loginuser"), 
    path('logout/',views.logout,name='logout'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)