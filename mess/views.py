from .models import UserProfile,Student,Vendor,Menu,Breakfast,Lunch,Dinner,Feedback,Receipt
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
import datetime
# Create your views here.






def home_view(request):
	return render(request,"mess/home.html")






def Login(request):
	return render(request , "mess/login.html")






def login_view(request):
	if request.method=="POST":		
		usernam = request.POST['username']
		passwor = request.POST['password']
		rol = request.POST['role']
		#if request.user.is_authenticated():
		try:
			user = UserProfile.objects.get(username=usernam, password=passwor,role =rol)
		except UserProfile.DoesNotExist:
			user=None
		if user is not None:
			print "user is not none"
			if (user.role == 'student'):
				login(request,user)
				return redirect("/student/")
			elif(user.role == 'vendor'):
				login(request,user)
				return redirect("/vendor/")
			elif(user.role == 'admin'):
				print "inside"
				login(request,user)
				print "after"
				return redirect("/admin/")
		else:
				# Return an 'invalid login' error message.
			return render(request , "mess/login.html" , {'unsuccess_message' :  'Authentication failed, Please try again',})
		#else:
		#	return render(request,"mess/NOtAuthenticate.html")
	else:
		return render(request,"mess/login.html")






def logout_view(request):
	print 'loggedout'
	logout(request)
	return redirect("/login/")




def student_view(request):
	if request.user.is_authenticated():
		usern = request.user.username
		user = UserProfile.objects.get(username=usern)
		
		if (user.role == "student"):
			
			return render(request,"mess/studentProfile.html",{'username' : request.user.username,'id' : user.student.ID,})
		else:
			return render(request,"mess/VendorProfile.html")
	else:
		return render(request,"mess/login.html")





def AddBalance(request):
	
	#print(add_balance)
	#print( type(add_balance))
	#print(request.Student.id)
	#request.Student.balance = request.Student.balance + add_balance
	#if request.user.is_authenticated():
	if request.user.is_authenticated():
		try:
			user = Student.objects.get(username=request.user.username, password=request.user.password ,role = 'student')
		except Student.DoesNotExist:
			user = None
		if user is not None:
			if 'add_balance' in request.POST:
				print (request.POST['add_balance'])
				if request.POST['add_balance']!="":
					user.balance = user.balance + int(request.POST['add_balance'])
					if (user.balance>12000):
						user.balance = user.balance - int(request.POST['add_balance'])
						return render(request,"mess/addBalance.html",{'username' : request.user.username,'unsuccess_message' : 'Not able to add Balance as it is going above 12000','id' : user.ID,})
				else:
					return render(request,"mess/addBalance.html",{'username' : request.user.username,'unsuccess_message' : 'please give valid balance','id' : user.ID,})
				print (user.balance)
				print (user.username)
				print (user.role)
				user.save()
				return render(request,"mess/addBalance.html",{'username' : request.user.username,'success_message' : 'Balance is successfully added','id' : user.ID,})
			else:
				return render(request,"mess/addBalance.html",{'username' : request.user.username,'id' : user.ID,})
		else:
			return render(request,"mess/VendorProfile.html")
	else:
		return render(request,"mess/login.html")







def DeductBalance(request):
	if request.user.is_authenticated():
		try:
			user = Vendor.objects.get(username=request.user.username, password = request.user.password ,role = 'vendor')
		except Vendor.DoesNotExist:
			user = None
		if user is not None:
			st = Student.objects.all()
			if 'student_id' in request.POST:
				print(request.POST['student_id'])
				StuID = request.POST['student_id']
				if 'deduct_amount' in request.POST:
					amoun = int(request.POST['deduct_amount'])
					for stu in user.student_set.all():
						if stu.ID == StuID:
							if stu.balance >= amoun:
								dat =  datetime.date.today()
								print 'date ', dat
								print 'amount',amoun
								try:
									print 'try'
									rec=Receipt.objects.get(date=dat,amount=amoun,stud=stu)
								except Receipt.DoesNotExist:
									print 'exception'
									rec=None	
								if rec is not None:
									print 'already'
									return render(request,"mess/DeductBalance.html",{'username' : request.user.username,'un_message' : 'User has already used today service','student' : st ,})
									
								else:
									rec=Receipt(date=dat,amount=amoun,stud=stu)
									rec.save()
									stu.balance = stu.balance - amoun
									stu.save()
								return render(request,"mess/DeductBalance.html",{'username' : request.user.username,'message' : 'Balance is successfully deducted','student' : st ,})
								#return SuccessMessage (amount equals to amoun is deducted
							else:
								return render(request,"mess/DeductBalance.html",{'username' : request.user.username,'un_message' : 'Balance is less than required','student' : st ,})
					else:
						return render(request,"mess/DeductBalance.html",{'username' : request.user.username,'un_message' : 'No student with that id','student' : st ,})
				else:
					return render(request,"mess/DeductBalance.html",{'username' : request.user.username,'student' : st ,})
			else:
					return render(request,"mess/DeductBalance.html",{'username' : request.user.username,'student' : st ,})
		else:
			return render(request,"mess/studentProfile.html",{'username' : request.user.username,})
	else:
		return render(request,"mess/login.html")








def view_balance(request):
	if request.user.is_authenticated():
		try:
			user = Student.objects.get(username=request.user.username, password=request.user.password ,role = 'student')
		except Student.DoesNotExist:
			user = None
		if user is not None:	
			print(user.balance)
			balanc = user.balance
			return render(request,"mess/ViewBalance.html",{'balance':balanc,'username':request.user.username,'id' : user.ID,})
		else:	
			return render(request,"mess/VendorProfile.html")
	else:
		return render(request,"mess/login.html")
	







def vendor_view(request):
	if request.user.is_authenticated():
		usern = request.user.username
		user = UserProfile.objects.get(username=usern)
		if (user.role == "vendor"):
			st = Student.objects.all()
			return render(request,"mess/VendorProfile.html",{'username' : request.user.username, 'student' : st ,})
		else:
			return render(request,"mess/studentProfile.html",{'username' : request.user.username,})
	else:
		return render(request,"mess/login.html")








def view_feedback(request):
	if request.user.is_authenticated():
		try:
			user = Vendor.objects.get(username=request.user.username, password=request.user.password ,role = 'vendor')
		except Vendor.DoesNotExist:
			user = None
		if user is not None:
			for stu in user.student_set.all():
				if Feedback.objects.count():
					print(Feedback.objects.count())
					feed = Feedback.objects.all()
					return render(request,"mess/ViewFeedback.html",{'username' : request.user.username,'feedback_exit' : 'Feedback of all students', 'feed' : feed ,})
			print("No feedback")
			return render(request,"mess/ViewFeedback.html",{'username' : request.user.username,'no_feedback' : 'feedback does not exit',})
		else:
			return render(request,"mess/studentProfile.html",{'username' : request.user.username,})
	else:
		return render(request,"mess/login.html")








def give_feedback(request):
	if request.user.is_authenticated():
		try:
			user = Student.objects.get(username=request.user.username, password=request.user.password ,role = 'student')
		except Student.DoesNotExist:
			user = None
		if user is not None:
			if 'give_feedback' in request.POST:
				print (request.POST['give_feedback'])
				feedback = request.POST['give_feedback']
				if not feedback:
					return render(request,"mess/GiveFeedback.html",{'username' : request.user.username,'emptyfeedback' : 'Can not send empty feedback','id' : user.ID,})
				else:
					if user is not None:	
						f = Feedback(feedbac = feedback,stu = user)	
						f.save()
						#user.feedBack.add(f)
						user.save()
						return render(request,"mess/GiveFeedback.html",{'username' : request.user.username,'feedback' : feedback ,'id' : user.ID,})
					else:
						return render(request,"mess/VendorProfile.html")
			else:
				return render(request,"mess/GiveFeedback.html",{'username' : request.user.username,'id' : user.ID,})
		else:
			return render(request,"mess/VendorProfile.html",{'username' : request.user.username})
	else:
		return render(request,"mess/login.html")







def view_menu_vendor(request):
	if request.user.is_authenticated():
		try:
			user = Vendor.objects.get(username=request.user.username, password=request.user.password ,role = 'vendor')
		except Vendor.DoesNotExist:
			user = None
		if user is not None:
		
			breakfas = Breakfast.objects.get(typeOf = 'breakfast') 
			lunc = Lunch.objects.get(typeOf = 'lunch')
			dinne = Dinner.objects.get(typeOf = 'dinner') 
			return render(request,"mess/ViewMenuVendor.html",{'breakfast':breakfas , 'lunch' : lunc , 'dinner' : dinne ,'username':request.user.username,})  
	else:
		return render(request,"mess/login.html")







def view_menu_student(request):
	if request.user.is_authenticated():
		try:
			user = Student.objects.get(username=request.user.username, password=request.user.password ,role = 'student')
		except Student.DoesNotExist:
			user = None
		if user is not None:
			breakfas = Breakfast.objects.get(typeOf = 'breakfast') #Have to relate to one object remember why use only one
			lunc = Lunch.objects.get(typeOf = 'lunch')#Have to relate to one object remember why use only one object
			dinne = Dinner.objects.get(typeOf = 'dinner') #Have to relate to one object remember why use only one object
			return render(request,"mess/ViewMenuStudent.html",{'breakfast':breakfas,'lunch':lunc,'dinner':dinne,'username':request.user.username,'id' : user.ID,})  
		else:
			return render(request,"mess/VendorProfile.html",{'username' : request.user.username})
	else:
		return render(request,"mess/login.html")

def delete_feedback(request):
	if request.user.is_authenticated():
		try:
			user = Vendor.objects.get(username=request.user.username, password=request.user.password ,role = 'vendor')
		except Vendor.DoesNotExist:
			user = None
		if user is not None:
			Id=request.POST['delete_feed']
			print 'id ' ,Id
			feed=Feedback.objects.all()
			for feedb in Feedback.objects.all():
				print 'feed back id' ,feedb.id
				if feedb.id == int(Id):
					print 'in side'
					feedb.number=0
					feedb.save()
					return render(request,"mess/ViewFeedback.html",{'username' : request.user.username,'feedback_exit' : 'Feedback of all students', 'feed' : feed ,})
			return render(request,"mess/ViewFeedback.html",{'username' : request.user.username,'feedback_exit' : 'id does not exist', 'feed' : feed ,})
		else:
			return render(request,"mess/studentProfile.html",{'username' : request.user.username,})

#def balance_confirmation(request):
#	if request.user.is_authenticated():
#		return redirect()
	


