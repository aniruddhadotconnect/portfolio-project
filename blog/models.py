from django.db import models

# Create a blog model
class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]
	
#Title
#date
#body
#Image


#Add the blog app to the settings


#Create a migration


#migrate


#add to the admin
