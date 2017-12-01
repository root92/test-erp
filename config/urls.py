"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from apps.core import views as core_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.index, name='index'),
    url(r'^login', auth_views.login, {'template_name': 'core/login.html'},
        name='login'),
    url(r'^home/$', core_views.home, name='home'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admission/', include('apps.admission.urls')),
    url(r'^dep_home/', include('apps.departement.urls')),
    # url(r'^student_list/', include('apps.students.urls')),
    
]


#add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]


# Change admin site title
admin.site.site_title = _("Administration de L'université")
# Change admin site header
admin.site.site_header = _("Administration de L'université")
# Change admin index header
admin.site.index_title = _("Administration de L'université")
