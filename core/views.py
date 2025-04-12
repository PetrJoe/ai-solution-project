from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import *

def home(request):
    solutions = Solution.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]
    upcoming_events = Event.objects.filter(date__gt=timezone.now()).order_by('date')[:3]
    latest_articles = Article.objects.order_by('-created_at')[:3]
    
    context = {
        'solutions': solutions,
        'testimonials': testimonials,
        'upcoming_events': upcoming_events,
        'latest_articles': latest_articles,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def solutions_list(request):
    solutions = Solution.objects.all()
    return render(request, 'core/solutions.html', {'solutions': solutions})

def solution_detail(request, pk):
    solution = get_object_or_404(Solution, pk=pk)
    return render(request, 'core/solution_detail.html', {'solution': solution})

def events(request):
    upcoming_events = Event.objects.filter(date__gt=timezone.now()).order_by('date')
    past_events = Event.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'core/events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    # Parse agenda items if they exist
    agenda_items = []
    if event.agenda:
        for line in event.agenda.splitlines():
            if line.strip():  # Skip empty lines
                # Assuming format like "10:00 Keynote Speech"
                if ':' in line and len(line) > 5:
                    time = line[:5]  # Get first 5 chars (time)
                    description = line[6:]  # Get rest after time
                    agenda_items.append({'time': time, 'description': description})
                else:
                    # Handle case where format is different
                    agenda_items.append({'time': '', 'description': line})
    
    # Get 3 related events (upcoming events excluding current one)
    related_events = Event.objects.filter(date__gt=timezone.now()).exclude(pk=event.pk).order_by('date')[:3]
    
    # Initialize the registration form
    form = EventRegistrationForm()
    
    context = {
        'event': event,
        'related_events': related_events,
        'form': form,
        'agenda_items': agenda_items,
    }
    
    return render(request, 'core/event_detail.html', context)

def event_registration(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            
            messages.success(request, "You have successfully registered for this event!")
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventRegistrationForm()
    
    context = {
        'event': event,
        'form': form,
    }
    
    return render(request, 'core/event_detail.html', context)

def gallery(request):
    galleries = Gallery.objects.all().order_by('-created_at')
    
    # Extract all images from all galleries
    images = GalleryImage.objects.all().order_by('-gallery__created_at')
    
    # Get recent events for the bottom section
    recent_events = Event.objects.filter(date__lt=timezone.now()).order_by('-date')[:3]
    
    context = {
        'galleries': galleries,
        'images': images,
        'recent_events': recent_events,
    }
    
    return render(request, 'core/gallery.html', context)

def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    images = gallery.images.all()  # Get all images for this gallery
    return render(request, 'core/gallery_detail.html', {'gallery': gallery, 'images': images})

def gallery_category(request, slug):
    # This is a placeholder - you'll need to add a Category model
    # For now, we'll just return all images
    images = GalleryImage.objects.all().order_by('-gallery__created_at')
    recent_events = Event.objects.filter(date__lt=timezone.now()).order_by('-date')[:3]
    
    context = {
        'images': images,
        'recent_events': recent_events,
        'category': {'slug': slug, 'name': slug.replace('-', ' ').title()}
    }
    
    return render(request, 'core/gallery.html', context)


def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'core/testimonials.html', {'testimonials': testimonials})

def articles(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'core/articles.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    # Get related articles (excluding the current one)
    related_articles = Article.objects.exclude(pk=pk).order_by('-created_at')[:3]
    
    return render(request, 'core/article_detail.html', {
        'article': article,
        'related_articles': related_articles
    })



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def request_demo(request):
    if request.method == 'POST':
        form = DemoRequestForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new DemoRequest object
            demo_request = form.save(commit=False)
            
            # Set default status
            demo_request.status = 'pending'
            
            # Save the demo request to the database
            demo_request.save()
            
            messages.success(request, 'Your demo request has been submitted. We will contact you to confirm the details.')
            return redirect('home')
    else:
        form = DemoRequestForm()
    return render(request, 'core/request_demo.html', {'form': form})

# Admin views
@login_required
def admin_dashboard(request):
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    pending_demos = DemoRequest.objects.filter(status='pending').count()
    upcoming_events = Event.objects.filter(date__gt=timezone.now()).count()
    
    # Get recent messages and demos for the dashboard
    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    recent_demos = DemoRequest.objects.all().order_by('-created_at')[:5]
    
    context = {
        'unread_messages': unread_messages,
        'pending_demos': pending_demos,
        'upcoming_events': upcoming_events,
        'recent_messages': recent_messages,
        'recent_demos': recent_demos,
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def admin_messages(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin/messages.html', {'messages': messages})

@login_required
def admin_message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    message.is_read = True
    message.save()
    return render(request, 'admin/message_detail.html', {'message': message})

@login_required
def admin_demo_requests(request):
    demos = DemoRequest.objects.all().order_by('-created_at')
    return render(request, 'admin/demo_requests.html', {'demos': demos})

@login_required
def admin_demo_detail(request, pk):
    demo = get_object_or_404(DemoRequest, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['pending', 'confirmed', 'completed', 'cancelled']:
            demo.status = status
            demo.save()
            messages.success(request, f'Demo request status updated to {status}')
    return render(request, 'admin/demo_detail.html', {'demo': demo})


