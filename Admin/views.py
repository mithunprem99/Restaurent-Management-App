from django.shortcuts import render,redirect
from Admin.models import*
from Manager.models import*
from User.models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def index(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(Booked_Status='pending',is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	
	feedback_tb=FeedbackModel.objects.all()
	return render(request,'index.html',{'views':food_tb,'events':event_tb,'table':table_tb,'feed':feedback_tb,'staff':staff_tb})

def login(request):
	return render(request,'login.html')


def loginAction(request):
	username=request.POST['username']
	password=request.POST['password']
	admin_tb=AdminModel.objects.filter(Username=username,Password=password)
	manager_tb=ManagerModel.objects.filter(Username=username,Password=password)
	user_tb=UserModel.objects.filter(Username=username,Password=password)
	if admin_tb.count()>0:
		request.session['Username']=admin_tb[0].Username

		request.session['id']=admin_tb[0].id 
		return render(request,'Adminhome.html')

	elif manager_tb.count()>0:
		request.session['id']=manager_tb[0].id
		request.session['Name']=manager_tb[0].Name
		request.session['Username']=manager_tb[0].Username
		
		return render(request,'managerHome.html')
	

	elif user_tb.count()>0:
		food_tb=FoodModel.objects.all()
		event_tb=EventModel.objects.all()
		table_tb=DinningModel.objects.filter(Booked_Status='pending',is_active='True')
		request.session['id']=user_tb[0].id
		request.session['Username']=user_tb[0].Username

		request.session['Name']=user_tb[0].Name
		return render(request,'userHome.html',{'views':food_tb,'events':event_tb,'table':table_tb})


	else:
		return redirect('login')

def adminhome(request):
	return render(request,'Adminhome.html')

def addManager(request):
	return render(request,'managerRegister.html')


def addmanagerAction(request):
	name=request.POST['name']
	address=request.POST['address']
	phone=request.POST['phone']
	gender=request.POST['gender']
	email=request.POST['email']
	dob=request.POST['dob']
	image=request.FILES.get('file')
	username=request.POST['username']
	password=request.POST['password']
	manager_tb=ManagerModel(Name=name,Address=address,Phone=phone,Email=email,Image=image,Username=username,Password=password,Gender=gender,DOB=dob)
	manager_tb.save()
	messages.add_message(request,messages.INFO,"Registration Sucessful")
	return redirect('addManager')


def checkMUserName(request):
	name=request.GET['rname']
	manager_tb=ManagerModel.objects.filter(Username=name)
	if len(manager_tb)>0:
		msg= "exist"
	else:
		msg= "not exist"
	return JsonResponse({'valid':msg})


def adminmanagerView(request):
	manager_tb=ManagerModel.objects.all()
	return render(request,'adminManagerview.html',{'view':manager_tb})



	



def editManager(request,id):
	manager_tb=ManagerModel.objects.filter(id=id)
	return render(request,'adminEditmanager.html',{'views':manager_tb})

def managerUpdateAction(request):
	id=request.POST['id']
	manager_tb=ManagerModel.objects.filter(id=id)
	name=request.POST['name']
	address=request.POST['address']
	gender=request.POST['gender']
	phone=request.POST['phone']
	dob=request.POST['dob']
	username=request.POST['username']
	email=request.POST['email']
	password=request.POST['password']
	if len(request.FILES)>0:
		file=request.FILES['file']
	else:
		file=manager[0].Image
	manager_tb=ManagerModel.objects.filter(id=id).update(Name=name,Address=address,Phone=phone,Email=email,Username=username,Password=password,Gender=gender,DOB=dob)
	manager_object=ManagerModel.objects.get(id=id)
	manager_object.Image=file
	manager_object.save()
	return redirect('adminmanagerView')


def deleteManager(request,id):
	manager_tb=ManagerModel.objects.filter(id=id).delete()
	return redirect('adminmanagerView')

def addstaff(request):
	return render(request,'adminAddstaffdetails.html')


def addstaffAction(request):
	name=request.POST['name']
	address=request.POST['address']
	phone=request.POST['phone']
	gender=request.POST['gender']
	email=request.POST['email']
	desg=request.POST['desg']
	dob=request.POST['dob']
	image=request.FILES.get('file')
	staff_tb=StaffModel(Name=name,Address=address,Phone=phone,Email=email,Image=image,Gender=gender,DOB=dob,Designation=desg)
	staff_tb.save()
	messages.add_message(request,messages.INFO,"Added Succesfully")
	return redirect('addstaff')

def viewStaff(request):
	staff_tb=StaffModel.objects.all()
	return render(request,'adminStafdetail.html',{'view':staff_tb})


def staffupdate(request,id):
	# staff=request.session['id']
	# staff_tb=StaffModel.objects.filter(id=staff)
	staff_tb=StaffModel.objects.filter(id=id)
	return render(request,'staffupdate.html',{'view':staff_tb})


def staffupdateAction(request):
	id=request.POST['id']
	staff_tb=StaffModel.objects.filter(id=id)
	name=request.POST['name']
	address=request.POST['address']
	gender=request.POST['gender']
	phone=request.POST['phone']
	dob=request.POST['dob']
	email=request.POST['email']
	desg=request.POST['desg']

	if len(request.FILES)>0:
		file=request.FILES['file']
	else:
		file=staff[0].Image
	staff_tb=StaffModel.objects.filter(id=id).update(Name=name,Address=address,Gender=gender,Phone=phone,Email=email,Designation=desg)
	staff_object=StaffModel.objects.get(id=id)
	staff_object.Image=file
	staff_object.save()
	return redirect('viewStaff')

def staffdelete(request,id):
	staff_tb=StaffModel.objects.filter(id=id).delete()
	return redirect('viewStaff')

def viewCustomerfood(request):
	order_tb=OrderModel.objects.all().order_by('-id')
	return render(request,'adminCustomerFooddetails.html',{'views':order_tb})

def viewOnlineCustomerfood(request):
	delivery_tb=DeliveryModel.objects.all().order_by('-id')
	return render(request,'adminCustomeronlineFooddetails.html',{'views':delivery_tb})




def viewReservations(request):
	reserv_tb=Reservation.objects.all().order_by('-id')
	return render(request,'viewReservation.html',{'views':reserv_tb})


def adminviewAttendance(request):
	present_tb=PresentModel.objects.all()
	absent_tb=AbsentModel.objects.all()
	return render(request,'adminviewAttendance.html',{'views':present_tb,'absent':absent_tb})

def adminsearchBydate(request):
	search=request.POST['date']
	att_tb=AttendanceModel.objects.filter(Date__istartswith=search)
	return render(request,'adminviewAttendance.html',{'views':att_tb})

def adminsearchOrderBydate(request):
	search=request.POST['date']
	att_tb=OrderModel.objects.filter(Date__istartswith=search)
	return render(request,'adminCustomerFooddetails.html',{'views':att_tb})

def adminsearchReservationBydate(request):
	search=request.POST['date']
	att_tb=OrderModel.objects.filter(Date__istartswith=search)
	return render(request,'viewReservation.html',{'views':att_tb})




def feedbacks(request):
	feedback_tb=FeedbackModel.objects.all().order_by('-id')
	return render(request,'customerfeedbacks.html',{'views':feedback_tb})


def viewcomplaints(request):
	complaint_tb=ComplaintModel.objects.all().order_by('-id')
	return render(request,'customercomplaints.html',{'views':complaint_tb})


def forgotpasswordone(request):
	return render(request,'forgotpassword1.html')

def forgotpasswordoneAction(request):
	username=request.POST['username']
	email=request.POST['email']
	dob=request.POST['dob']
	user_tb=UserModel.objects.filter(Username=username,Email=email,DOB=dob)
	if len(user_tb)>0:
		return render(request,'newpassword.html',{'data':username})

	else:
		messages.add_message(request,messages.INFO,"Incorrect Data")

		return redirect('login')


def newpasswordAction(request):
	username=request.POST['username']
	password=request.POST['password']
	repass=request.POST['confirm']
	if password == repass:
		user_tb=UserModel.objects.filter(Username=username)
		user_tb.update(Password=password)
		messages.add_message(request,messages.INFO,"Password Updated Succesfully")
		return render(request,'login.html',{'data':username})
	else:
		messages.add_message(request,messages.INFO,"Password Not Match")
		return redirect('login')





def checkUserName(request):

	name=request.POST['name']
	manager_tb=ManagerModel.objects.filter(Username=name)
	if len(manager_tb)>0:
		msg="exist"
	else:
		msg='not exist'
	return JsonResponse({'valid':msg})


def msgforward(request,id):
	complaint_tb=ComplaintModel.objects.filter(id=id).update(Status='forwarded')
	
	messages.add_message(request,messages.INFO,"Complaints Forwarded")
	return redirect('viewcomplaints')


def replayComplaints(request,id):
	complaint_tb=ComplaintModel.objects.filter(id=id)
	return redirect('viewcomplaints')


def replayComplaintsAction(request):
	complaint=request.POST['id']
	message=request.POST['message']
	receiver=request.POST['userid']
	reply_tb=ReplayModel(Message=message,Complaint_id=complaint,User_id=receiver)
	reply_tb.save()
	messages.add_message(request,messages.INFO,"Message sent")
	return redirect('viewcomplaints')

