from django.urls import path
from .views import *
from .dashboard import *

urlpatterns = [
    # Public pages
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('solutions/', solutions_list, name='solutions'),
    path('solutions/<int:pk>/', solution_detail, name='solution_detail'),
    path('events/', events, name='events'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/<int:event_id>/register/', event_registration, name='event_registration'),

    path('gallery/', gallery, name='gallery'),
    path('gallery/<int:pk>/', gallery_detail, name='gallery_detail'),
    path('gallery/category/<slug:slug>/', gallery_category, name='gallery_category'),

    path('testimonials/', testimonials, name='testimonials'),
    path('articles/', articles, name='articles'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('contact/', contact, name='contact'),
    path('request-demo/', request_demo, name='request_demo'),
    
    # Custom Admin Dashboard
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/messages/', admin_messages, name='admin_messages'),
    path('dashboard/messages/<int:pk>/', admin_message_detail, name='admin_message_detail'),
    path('dashboard/demo-requests/', admin_demo_requests, name='admin_demo_requests'),
    path('dashboard/demo-requests/<int:pk>/', admin_demo_detail, name='admin_demo_detail'),
    path('dashboard/events/', admin_events, name='admin_events'),
    path('dashboard/analytics/', admin_analytics, name='admin_analytics'),
]
