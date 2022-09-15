from django.urls import path
from . import views
from users import views as u_views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:subject_id>", views.subject, name="subject"),
    path('users', u_views.index, name="users")
]