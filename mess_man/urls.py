"""mess_man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mess.views import login_view,student_view,AddBalance,view_balance,vendor_view,view_feedback,give_feedback,DeductBalance,view_menu_vendor,view_menu_student,home_view,Login,logout_view,delete_feedback

urlpatterns = [
	#url(r'^/admin/$', lambda x: HttpResponseRedirect('/mysite/admin/myapp/')),
	url(r'^admin/', admin.site.urls,name = "admin"),
	url(r'^$',home_view,name = "home"),
	url(r'^login/$',Login,name = "login"),
	url(r'^logout/$',logout_view,name = "logout"),
	url(r'^login_page/$',login_view,name = 'login_page'),
	url(r'^student/$',student_view,name = 'student'),
	url(r'^student/add_balance/$',AddBalance,name = 'Add_balance'),
	url(r'^student/view_balance/$',view_balance,name = 'view_balance'),
	url(r'^vendor/$',vendor_view,name = 'vendor'),
	url(r'^vendor/view_feedback/$',view_feedback,name = 'view_feedback'),
	url(r'^student/give_feedback/$',give_feedback,name = 'give_feedback'),
	url(r'^vendor/deduct_balance/$', DeductBalance, name = 'Deduct_balance'),
	url(r'^vendor/view_menu_vendor/$', view_menu_vendor, name = 'view_menu_vendor'),
	url(r'^student/view_menu_student/$',view_menu_student, name = 'view_menu_student'),
	url(r'^vendor/delete_feedback/$',delete_feedback,name= 'delete_feedback'),
	#url(r'^vendor/confirmation/$',balance_confirmation,name='confirmation'),

		
]
