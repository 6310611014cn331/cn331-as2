from django.urls import path, include
from . import views
from subject import views as s_views

urlpatterns = [
    path('', views.index, name='u_index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('subject', s_views.index, name='subject'),
    path('<username>/quotas', views.quotas, name='quotas'),
    path('<username>/book', views.book, name='book'),
    path('<username>/<int:s_id>/delete', views.delete, name='delete')
]