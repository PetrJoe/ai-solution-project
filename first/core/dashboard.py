from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count
from django.http import JsonResponse
from .models import Event, Gallery, Solution, Testimonial, ContactMessage, DemoRequest, Article

@staff_member_required
def admin_dashboard(request):
    # Count statistics
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    pending_demos = DemoRequest.objects.filter(status='pending').count()
    upcoming_events = Event.objects.filter(date__gt=timezone.now()).count()
    total_solutions = Solution.objects.count()
    total_testimonials = Testimonial.objects.count()
    total_galleries = Gallery.objects.count()
    total_articles = Article.objects.count()
    
    # Recent items
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    recent_demo_requests = DemoRequest.objects.order_by('-created_at')[:5]
    recent_events = Event.objects.order_by('-date')[:5]
    
    # Demo requests by status
    demo_status_counts = DemoRequest.objects.values('status').annotate(count=Count('status'))
    
    context = {
        'unread_messages': unread_messages,
        'pending_demos': pending_demos,
        'upcoming_events': upcoming_events,
        'total_solutions': total_solutions,
        'total_testimonials': total_testimonials,
        'total_galleries': total_galleries,
        'total_articles': total_articles,
        'recent_messages': recent_messages,
        'recent_demo_requests': recent_demo_requests,
        'recent_events': recent_events,
        'demo_status_counts': demo_status_counts,
    }
    return render(request, 'admin/dashboard.html', context)

@staff_member_required
def admin_messages(request):
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin/messages.html', {'messages': messages_list})

@staff_member_required
def admin_message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'admin/message_detail.html', {'message': message})

@staff_member_required
def admin_demo_requests(request):
    demos = DemoRequest.objects.all().order_by('-created_at')
    return render(request, 'admin/demo_requests.html', {'demos': demos})

@staff_member_required
def admin_demo_detail(request, pk):
    demo = get_object_or_404(DemoRequest, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['pending', 'confirmed', 'completed', 'cancelled']:
            demo.status = status
            demo.save()
            messages.success(request, f'Demo request status updated to {status}')
    return render(request, 'admin/demo_detail.html', {'demo': demo})

@staff_member_required
def admin_events(request):
    upcoming = Event.objects.filter(date__gt=timezone.now()).order_by('date')
    past = Event.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'admin/events.html', {'upcoming_events': upcoming, 'past_events': past})

@staff_member_required
def admin_analytics(request):
    # Messages over time
    messages_by_date = ContactMessage.objects.extra(select={'date': 'date(created_at)'}).values('date').annotate(count=Count('id')).order_by('date')
    
    # Demo requests by status
    demo_status = DemoRequest.objects.values('status').annotate(count=Count('status'))
    
    # Events by month
    events_by_month = Event.objects.extra(select={'month': "to_char(date, 'YYYY-MM')"}).values('month').annotate(count=Count('id')).order_by('month')
    
    context = {
        'messages_by_date': list(messages_by_date),
        'demo_status': list(demo_status),
        'events_by_month': list(events_by_month),
    }
    return render(request, 'admin/analytics.html', context)
