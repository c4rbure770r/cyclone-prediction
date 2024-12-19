from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('recent_alerts/', views.recent_alerts_view, name='recent_alerts'),
    path('add_alert/', views.add_alert_view, name='add_alert'),
    path('delete_alert/<int:alert_id>/', views.delete_alert_view, name='delete_alert'),
    path('edit_alert/<int:alert_id>/', views.edit_alert_view, name='edit_alert'),
    path('temparatures/', views.temparatures_view, name='temparatures'),
    path('cyclone_prediction/', views.cycloneprediction_view, name='cyclone_prediction'),
]
