"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView
from knittingstore.views import RegisterView, logout, TermsAndConditionsView, PrivacyPolicyView
# from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/knitting/')),  # Redirect from "/" to "/knitting/"
    path('knitting/', include("knittingstore.urls")),
     # auth
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),  # URL for registration
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('logout/', logout, name='logout'),
    path('support/terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms-and-conditions'),
    path('support/privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),

    # path('logout-confirmation/', LogoutConfirmationView.as_view(), name='logout_confirmation'),
    # Include Django authentication URLs
    # path('accounts/', include('django.contrib.auth.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)