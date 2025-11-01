from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile



class UserAdmin(admin.ModelAdmin):
    model = User
    #only display username field
    fields = ["username"]


admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
