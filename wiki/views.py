from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context

#required for create page
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from wiki.models import DefaultPage, Page, LearningObject

# Create your views here.


class createPage(CreateView):
	model = Page
	template_name = 'wiki/edit_page.html'
	def get_success_url(self):
		return reverse('index')

def index(request):
	context = RequestContext(request)
	defaultpages_list = DefaultPage.objects.order_by('edited_date')
	context_dict = {'defaultpages':defaultpages_list}
	return render_to_response('wiki/index.html', context_dict, context)