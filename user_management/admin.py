from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'user_id', 'creation_date']
    search_fields = ['username', 'email', 'phone', 'user_id']
    readonly_fields = ['creation_date']

admin.site.register(User, UserAdmin)
