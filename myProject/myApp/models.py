from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class user(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	DOB = models.DateField()
	Phone = models.IntegerField()
	email = models.EmailField()
	Address = models.CharField(max_length=255)
	City = models.CharField(max_length=255)
	Country = models.CharField(max_length=255)
	ZipCode = models.CharField(max_length=255)
	Password = models.CharField(max_length=255)
	Image = models.CharField(max_length=255)
	
 
def __str__(self):
    	return self.FirstName
class enquiry(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	Email = models.EmailField()
	PhoneNumber = models.IntegerField()
	Message = models.CharField(max_length=255)

	def __str__(self):
         return self.FirstName

class Review(models.Model):
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    # def edit(self, new_description):
    #     self.description = new_description
    #     self.save()

    # def delete(self):
    #     super().delete()
