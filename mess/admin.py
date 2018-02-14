from django.contrib import admin
from .models import Student,Vendor,Breakfast,Lunch,Dinner,Feedback,UserProfile,Admin
# Register your models here.

admin.site.register(Student)
admin.site.register(Vendor)

##
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)

admin.site.register(Feedback)
admin.site.register(UserProfile)
admin.site.register(Admin)
#####s

#admin.site.register(UserProfile)


