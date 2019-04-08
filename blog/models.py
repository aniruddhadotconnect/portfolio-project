from django.db import models

# Create a blog model
class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	
#Title
#date
#body
#Image


#Add the blog app to the settings


#Create a migration


#migrate


#add to the admin
