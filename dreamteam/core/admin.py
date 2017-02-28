from django.contrib import admin
from dreamteam.core.models import (UserMember, Team)
from dreamteam.core.forms import (UserMemberForm, TeamForm)

# Register your models here.
class UserMemberAdmin(admin.ModelAdmin):
    form = UserMemberForm
    list_display = ('first_name', 'last_name', 'email', 'password', 'created_at')
    date_hierarchy = 'created_at'
    list_filter = ('email',)
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(UserMember, UserMemberAdmin)

class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    list_display = ('name', 'created_at')
    date_hierarchy = 'created_at'
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Team, TeamAdmin)
