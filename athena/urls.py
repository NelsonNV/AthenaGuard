from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.static import serve
from django.conf import settings
from .views import *



urlpatterns = [
    # Paginas Basicas
    path('login', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('vulneravilidad/add/', add_vulnerabilidad, name='addVuln'),
    path('vulneravilidad/list/', list_vulnerabilidad, name='listVuln'),
    path('vulneravilidad/edit/<int:id>/', edit_vulnerabilidad, name='editVuln'),
    path('vulneravilidad/delete/<int:id>/', delete_vulnerabilidad, name='deleteVuln'),


]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
]