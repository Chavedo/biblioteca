from django.urls.conf import re_path
from apps.usuario.views import Inicio, Login, logout_usuario
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include(('apps.libro.urls', 'libro'))),
    path('usuario/', include(('apps.usuario.urls', 'usuario'))),
    path('', Inicio.as_view(), name='index'),
    path('accounts/login/', Login.as_view(), name="login"),
    path('logout/', login_required(logout_usuario), name='logout')
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]