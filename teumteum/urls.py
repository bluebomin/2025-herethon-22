from django.contrib import admin
from django.urls import path, include  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),              
    path('accounts/', include('accounts.urls')),    
    path('post/', include('post.urls')),            
    path('plan/', include('plan.urls')),            
    path('jobs/', include('jobs.urls')), 
    path('', include('home.urls')),
    path('my/', include('my.urls')),
    path('counsel/', include('counsel.urls')),
    path('alumna/', include('alumna.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)