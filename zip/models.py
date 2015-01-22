from django.db import models
#create slugs for zips
from django.template.defaultfilters import slugify

#need zipfile to unpack archive
import zipfile, os,fnmatch

# Create your models here.

class LearningObject(models.Model):
	title = models.CharField(max_length=100)
	archivefile = models.FileField(upload_to='learningobject/archivefiles/%Y/%m/%d')
	indexpath = models.CharField(max_length=254,editable=False)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	edited_date =  models.DateTimeField(auto_now_add=False,auto_now=True)
	slug = models.SlugField(max_length=100,editable=False,blank=True)
	def __unicode__ (self): 
		return self.title
	def unpackarchive(self):
		filename = (self.archivefile)
		folder = str(filename.split(".")[0])
		with zipfile.ZipFile(file,"r") as z:
			for each in z.namelist():
				if each == "index.html" or each == "index.htm":
					index_found = "True"
				else:
					pass
			if not index_found:
				print "zip file does not contain a valid index.html file"
			else:
				path = os.path.join("learningobject","archivefiles",folder)
				z.extractall(path)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(LearningObject, self).save(*args, **kwargs)
