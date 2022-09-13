from django.db import models

# Create your models here.
#makemigrations=create changes and store in a file
#migrate=apply the pending changes created by makemigrations
class Contact(models.Model):
  
  email = models.CharField(max_length=122)
  desc = models.TextField()
  date = models.DateField()
  def __str__(self):
      return self.email
