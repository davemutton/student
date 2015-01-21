from django.db import models
#create slugs for pages
from django.template.defaultfilters import slugify

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	edited_date =  models.DateTimeField(auto_now_add=False,auto_now=True)
	child_pages = models.ManyToManyField("self",blank=True,editable=False)
	slug = models.SlugField(max_length=100,editable=False,blank=True)
	def __unicode__ (self): 
		return self.title
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Page, self).save(*args, **kwargs)