from django.contrib import admin
from .models import Thread, User, Reply

class ThreadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('topic',)}

admin.site.register(User)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply)