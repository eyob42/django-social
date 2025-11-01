from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile


# Define an inline admin class to embed Profile editing inside the User admin page
class ProfileInline(admin.StackedInline):
    model = Profile  # This tells Django which model to inline


class UserAdmin(admin.ModelAdmin):
    model = User
    #only display username field
    fields = ["username"]
    inlines = [ProfileInline]



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
