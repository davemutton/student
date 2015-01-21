from django.contrib import admin
from wiki.models import Page
from django_summernote.admin import SummernoteModelAdmin
class PageAdmin(SummernoteModelAdmin):
	pass


# Register your models here.
admin.site.register(Page,PageAdmin)