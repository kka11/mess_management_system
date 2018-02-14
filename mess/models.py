from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import models as mods
# Create your models here.

class UserProfile(mods.User):
	role = models.CharField(max_length=10,null=True)
class Admin(UserProfile):
	def __str__(self):
		return self.username + ' - ' + self.role 
class Vendor(UserProfile):
	#User.credential.role = 'vendor'

	#
	#
	#

	#deduct balance
	


	#
 	#
	#
	def __str__(self):
		return self.username + ' - ' + self.role


class Student(UserProfile):
	#role = 'student'on_delete=models.CASCADE
	#user = models.ForeignKey(UserProfile,null=True,default = 'fef')
	balance = models.IntegerField(default = 0)
 	#feedBack = models.ManyToManyField(Feedback)
	stud = models.ForeignKey(Vendor,null = True)
	ID = models.CharField(max_length = 10, blank = True)
	#receipt = models.ForeignKey(Receipt,null =True,on_delete=models.CASCADE)
	def __str__(self):
		return self.username + ' - ' + self.role 


class Receipt(models.Model):
	#time = models.TimeField(max_length = 1000,null = True)
	date = models.DateField(max_length = 1000,null = True)
	amount = models.IntegerField()
	stud = models.ForeignKey(Student,null =True,on_delete=models.CASCADE)





class Feedback(models.Model):
	#feedback = models.ForeignKey(Student,null = True,on_delete=models.CASCADE)
	feedbac = models.CharField(max_length = 1000,null = True)
	number = models.IntegerField(default=1)
	stu = models.ForeignKey(Student,null =True,on_delete=models.CASCADE)
	




class Menu(models.Model):
	daily = models.CharField(max_length=500)
	sunday = models.CharField(max_length=500)
	monday = models.CharField(max_length=500)
	tuesday = models.CharField(max_length=500)
	wednesday = models.CharField(max_length=500)
	thrusday = models.CharField(max_length=500)
	friday = models.CharField(max_length=500)
	saturday = models.CharField(max_length=500)	
	
	class Meta:
		abstract = True

class Breakfast(Menu):
	typeOf = models.CharField(max_length=10)
	#sunday = models.Charfield(max_length=250)
	#monday = models.Charfield(max_length=250)
	#tuesday = models.Charfield(max_length=250)
	#wednesday = models.Charfield(max_length=250)
	#thrusday = models.Charfield(max_length=250)
	#friday = models.Charfield(max_length=250)
	#saturday = models.Charfield(max_length=250)

class Lunch(Menu):
	typeOf = models.CharField(max_length=10)
	#sunday = models.Charfield(max_length=250)
	#monday = models.Charfield(max_length=250)
	#tuesday = models.Charfield(max_length=250)
	#wednesday = models.Charfield(max_length=250)
	#thrusday = models.Charfield(max_length=250)
	#friday = models.Charfield(max_length=250)
	#saturday = models.Charfield(max_length=250)

class Dinner(Menu):
	typeOf = models.CharField(max_length=10)
	#sunday = models.Charfield(max_length=250)
	#monday = models.Charfield(max_length=250)
	#tuesday = models.Charfield(max_length=250)
	#wednesday = models.Charfield(max_length=250)
	#thrusday = models.Charfield(max_length=250)
	#friday = models.Charfield(max_length=250)
	#saturday = models.Charfield(max_length=250)





