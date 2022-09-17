from django.contrib import admin
from .models import user_quotas
# Register your models here.
class user_quotasAdmin(admin.ModelAdmin):
    filter_horizontal = ["subject"]

admin.site.register(user_quotas, user_quotasAdmin)