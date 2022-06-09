from django.contrib import admin
from .models import Question, Options,User

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question)
admin.site.register(Options)
admin.site.register(User)