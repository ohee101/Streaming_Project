from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from Its_Streaming_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('videos/', include('Its_Streaming_App.urls')),
    path('', views.home, name='home'),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)