from django.contrib import admin
from .models import Orders

# Register your models here.

@admin.register(Orders)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','book_id','address')