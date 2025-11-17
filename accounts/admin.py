from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'store_name', 'is_verified', 'created_at')
    list_filter = ('role', 'is_verified', 'created_at')
    search_fields = ('user__username', 'store_name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Info', {'fields': ('user', 'role')}),
        ('Store Info', {'fields': ('store_name', 'store_description')}),
        ('Contact', {'fields': ('phone_number', 'email')}),
        ('Address', {'fields': ('address', 'city', 'country')}),
        ('Profile', {'fields': ('profile_image', 'is_verified')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    
    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'
