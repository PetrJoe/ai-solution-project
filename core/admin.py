from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Gallery, GalleryImage, Solution, Testimonial, ContactMessage, DemoRequest, Article

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="auto" />', obj.image.url)
        return "No Image"

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_upcoming')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'

class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('title', 'created_at', 'image_count')
    search_fields = ('title', 'description')
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Number of Images'

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title', 'description', 'features')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image'

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'content_preview')
    search_fields = ('name', 'company', 'content')
    
    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content Preview'

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    
    def has_add_permission(self, request):
        return False
    
    def save_model(self, request, obj, form, change):
        if 'is_read' in form.changed_data:
            super().save_model(request, obj, form, change)

class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'preferred_date', 'preferred_time', 'status')
    list_filter = ('status', 'preferred_date')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
    date_hierarchy = 'preferred_date'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'title': ('title',)}

admin.site.register(Event, EventAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(DemoRequest, DemoRequestAdmin)
admin.site.register(Article, ArticleAdmin)

# Customize admin site
admin.site.site_header = "AI-Solutions Admin"
admin.site.site_title = "AI-Solutions Admin Portal"
admin.site.index_title = "Welcome to AI-Solutions Admin Portal"
