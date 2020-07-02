from django.contrib import admin

from .models import Poll



class PollAdmin(admin.ModelAdmin):
	list_display = ['question']
admin.site.register(Poll, PollAdmin)