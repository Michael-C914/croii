from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import documents
from user.models import UserJuridic, UserNatural, CustomUser


# Create your models here.
class Category(models.Model): 
	name_category = models.CharField()

	def __str__(self) -> str:
			return str(self.name_category)

class Project(models.Model): 
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
	user_admin = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=50)
	address = models.TextField()
	state = models.CharField(max_length=15)

	def __str__(self) -> str:
    		return str(self.name)

class Request(models.Model): 
	user_juridic = models.ForeignKey(UserJuridic, null=True, blank=True, on_delete=models.SET_NULL)
	user_natural = models.ForeignKey(UserNatural, null=True, blank=True, on_delete=models.SET_NULL)
	proyect_integer = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
	description = models.TextField()
	type_documents = models.CharField(choices=documents, default='P')
	is_juridic = models.BooleanField()
	is_natural = models.BooleanField()
	email = models.CharField(max_length=15)
	phone = models.IntegerField(max_length=9)
	conditions =  models.BooleanField()
	date = models.DateField()
	importance = models.CharField(max_length=15) 


	def __str__(self) -> str:
        	return str(self.id)

class DocumentProject(models.Model):
	request_id = models.ForeignKey(Request, null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to="documents", null=True)

	def __str__(self) -> str:
        	return str(self.id)

class DocumentAction(models.Model):
	request_id = models.ForeignKey(Request, null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to="documents", null=True)

	def __str__(self) -> str:
        	return str(self.id)

class DocumentInvestment(models.Model):
	request_id = models.ForeignKey(Request, null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to="documents", null=True)

	def __str__(self) -> str:
        	return str(self.id)

class DocumentBond(models.Model):
	request_id = models.ForeignKey(Request, null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to="documents", null=True)

	def __str__(self) -> str:
        	return str(self.id)

class Media(models.Model):
	project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
	image = image = models.ImageField(upload_to="image", null=True)

	def __str__(self) -> str:
        	return str(self.project.name)

