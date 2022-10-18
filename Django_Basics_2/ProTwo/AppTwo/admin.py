from django.contrib import admin

from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['email','first_name','last_name']

    search_fields=['first_name']

    list_filter=['first_name']

    list_display = ['first_name','email','last_name']

    list_editable = ['last_name']


admin.site.register(User,UserAdmin)
