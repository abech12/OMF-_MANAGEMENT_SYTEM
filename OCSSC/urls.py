"""OCSSC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static 

from django.contrib import admin
from django.urls import path
from django.urls import path,include,re_path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,)
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("branchs/",include("branchs.urls")), 
    path("accounts/",include("accounts.urls")), 
    path("loan/",include("loan.urls")), 
    path("",TemplateView.as_view(template_name="index.html")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.api_urls')),
    path('api/branchs/', include('branchs.api_urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
