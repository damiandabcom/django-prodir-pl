"""ds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView, RedirectView

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^posrednicy/', include('profiles.urls', namespace='profiles')),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='panel', permanent=False)),
    url(r'^$', views.home, name='home'),
    url(r'^o-nas/$', views.about, name='about'),
    url(r'^kontakt/$', views.contact, name='contact'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^polityka-prywatnosci/$', views.policy, name='policy'),
    url(r'^regulamin/$', views.toc, name='toc'),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)