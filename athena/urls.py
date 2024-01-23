from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.static import serve
from django.conf import settings
from .views import home, add_vulnerabilidad



urlpatterns = [
    # Paginas Basicas
    path('login', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('vulneravilidad/add', add_vulnerabilidad, name='addVuln'),

]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
]