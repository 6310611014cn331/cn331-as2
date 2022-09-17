from django.contrib import admin
from .models import detail, quotas

# Register your models here.
class detailAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "name", "section", "semester", "year"]
class quotasAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "days", "time", "sit"]

admin.site.register(detail, detailAdmin)
admin.site.register(quotas, quotasAdmin)