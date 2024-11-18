from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'can_create_post')
    list_editable = ('can_create_post',)
    search_fields = ('user__username',)

admin.site.register(Profile, ProfileAdmin)
