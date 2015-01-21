from django.shortcuts import render
#required for create page
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from wiki.models import Page

# Create your views here.


class createPage(CreateView):
	model = Page
	template_name = 'wiki/edit_page.html'
	def get_success_url(self):
		return reverse('index')