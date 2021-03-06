from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name="new"),
    path('create/', views.create, name='create'),
    path('slidebanner/', views.slidebanner, name="slidebanner"),
    path('<int:pk>/edit',views.edit, name='edit'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
