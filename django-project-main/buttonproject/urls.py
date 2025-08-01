"""
URL configuration for buttonproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('student/', views.student,name='student'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('faculty/', views.faculty_list, name='faculty'),
    path('events/', views.events_list, name='events'),
    path('faculty/<int:pk>/', views.faculty_detail, name='faculty_detail'),
    path('about/', views.about, name='about'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)