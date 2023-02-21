from django.shortcuts import render,redirect
from Admin.models import*
from Manager.models import*
from User.models import *
import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


# def checkUserName(request):
# 	name=request.POST['name']
# 	manager_tb=ManagerModel.objects.filter(Username=name)
# 	if len(manager_tb)>0:
# 		msg="exist"
# 	else:
# 		msg='not exist'
# 	return JsonResponse({'valid':msg})

def addFood(request):
	return render(request,'Addfood.html')

def addFoodAction(request):
	name=request.POST['food']
	image=request.FILES.get('file')
	price=request.POST['price']
	details=request.POST['details']
	cat=request.POST['cat']
	food_tb=FoodModel(Food=name,Image=image,Price=price,Details=details,Category=cat)
	food_tb.save()
	messages.add_message(request,messages.INFO,"Food item added successfully")
	return redirect('addFood')


def viewFood(request):
	food_tb=FoodModel.objects.all()
	return render(request,'managerviewFood.html',{'view':food_tb})


def updateFood(request,id):
	food_tb=FoodModel.objects.filter(id=id)
	return render(request,'editaddedFood.html',{'view':food_tb})


def updateFoodAction(request):
	id=request.POST['id']
	food=FoodModel.objects.filter(id=id)
	name=request.POST['food']
	price=request.POST['price']
	details=request.POST['details']
	if len(request.FILES)>0:
		file=request.FILES['file']
	else:
		file=food[0].Image
	food_tb=FoodModel.objects.filter(id=id).update(Food=name,Price=price,Details=details)
	food_object=FoodModel.objects.get(id=id)
	food_object.Image=file
	food_object.save()
	messages.add_message(request,messages.INFO,"Food item updated successfully")
	return redirect('viewFood')



def deleteFood(request,id):
	food_tb=FoodModel.objects.filter(id=id).delete()
	return redirect('viewFood')


def adminMessage(request):
	complaint_tb=ComplaintModel.objects.filter(Status='forwarded').order_by('-id')
	return render(request,'managerUsercomplaintview.html',{'comp':complaint_tb})




def dinningTables(request):
	dinning_tb=DinningModel.objects.all()
	order_tb=OrderModel.objects.all()
	return render(request,'addDiningtables.html',{'views':dinning_tb,'table':order_tb})


def dinningTablesAction(request):
	name=request.POST['name']
	chair=request.POST['chair']
	image=request.FILES.get('file')
	dinning_tb=DinningModel(Name=name,Chair=chair,Image=image)
	dinning_tb.save()
	return redirect('dinningTables')

def deleteTable(request,id):
	dinning_tb=DinningModel.objects.filter(id=id).delete()
	return redirect('dinningTables')

def dinningActivateAction(request):
	activate=request.POST.getlist('activate')
	for aid in activate:
		table_id=DinningModel.objects.filter(id=aid).update(is_active='True')
		# active=table_id[0].is_active
		# active.update(is_active='True')
		# return redirect('dinningTables')
	return redirect('dinningTables')


def addEvents(request):
	return render(request,'events.html')


def addEventsAction(request):
	name=request.POST['name']
	org=request.POST['org']
	date=request.POST['date']
	details=request.POST['details']
	event_tb=EventModel(Name=name,Organizer=org,Date=date,Details=details)
	event_tb.save()
	messages.add_message(request,messages.INFO,"Event added successfully")
	return redirect('addEvents') 


def eventManage(request):
	event_tb=EventModel.objects.all()
	return render(request,'manageEvents.html',{'views':event_tb})


def updateEvent(request,id):
	event_tb=EventModel.objects.filter(id=id)
	return render(request,'editEvents.html',{'views':event_tb})
	
def updateEventAction(request):
	id=request.POST['id']
	event_tb=EventModel.objects.filter(id=id)
	name=request.POST['name']
	org=request.POST['org']
	date=request.POST['date']
	details=request.POST['details']
	event_tb=EventModel.objects.filter(id=id).update(Name=name,Organizer=org,Date=date,Details=details)
	messages.add_message(request,messages.INFO,"Event updated successfully")
	return redirect('eventManage')


def deleteEvent(request,id):
	event_tb=EventModel.objects.filter(id=id).delete()
	return redirect('eventManage')


def viewFoodOrder(request):
	order_tb=BookModel.objects.filter(Status='pending')
	return render(request,'customerOrder.html',{'views':order_tb})


def confirmOrder(request,id):
	order_tb=OrderModel.objects.filter(Order_id=id)
	order=str(order_tb[0].Order_id)
	for f in order_tb:
		food_tb=FoodModel.objects.filter(Food=f)
		print(food_tb)
	# food_tb=FoodModel.objects.filter(id=food)
	for name in food_tb:

		fod=food_tb[0].Food
		print(fod)
	# for f in name:
	# 	print(f)
	print(order)
	book_tb=BookModel.objects.filter(id=id)
	book_tb.update(Status='Order Confirmed')
	order_tb.update(Status='Order Confirmed')
	user_tb=order_tb[0].User_id
	email=UserModel.objects.filter(id=user_tb)
	name=str(email[0].Name)
	mail=str(email[0].Email)
	# print(user_tb[0].Email)
	print(email)
	print(mail)
	print(name)
# 	send_mail(
#     'YOUR ORDER HAS BEEN CONFIRMED', #subject goes here
#     'Sir'+name+',' '\nyour order has been confirmed with the order ID'+order, #Message goes here
#     'jelori9693@prolug.com', #temp mail from temp mail.org[from mail]
#     [mail],# to mail
#     fail_silently=False,
# )
	return redirect('viewFoodOrder')

def reservation(request):
	reserv_tb=Reservation.objects.all()
	return render(request,'customerTable.html',{'views':reserv_tb})


def tableActivate(request,id):
	reserv_tb=DinningModel.objects.filter(id=id)
	reserv_tb.update(Booked_Status='pending')
	return redirect('dinningTables')

def tableDeactivate(request,id):
	reserv_tb=DinningModel.objects.filter(id=id)
	reserv_tb.update(Booked_Status='Booked')
	return redirect('dinningTables')


def addStock(request):
	stock_tb=StockModel.objects.all()
	return render(request,'addStock.html',{'views':stock_tb})


def addStockAction(request):
	name=request.POST['name']
	quantity=request.POST['quantity']
	stock_tb=StockModel(Item=name,Quantity=quantity)
	stock_tb.save()
	return redirect('addStock')

def Stockupdate(request,id):
	stock_tb=StockModel.objects.filter(id=id)
	return render(request,'stockUpdate.html',{'views':stock_tb})

	# name=request.POST['name']
	# quantity=request.POST['quantity']
	# stock=StockModel.objects.filter(id=id).update(Item=name,Quantity=quantity)

def StockupdateAction(request):
	id=request.POST['id']
	name=request.POST['name']
	quantity=request.POST['quantity']
	stock=StockModel.objects.filter(id=id).update(Item=name,Quantity=quantity)
	return redirect('addStock')

def deleteStock(request,id):
	stock=StockModel.objects.filter(id=id).delete()
	return redirect('addStock')

def staffAttendance(request):
	staff_tb=StaffModel.objects.all()
	return render(request,'attendance.html',{'views':staff_tb})




def viewConfirmedOrder(request):
	order_tb=OrderModel.objects.all().order_by('-id')
	return render(request,'viewconfirmedOrder.html',{'view':order_tb})

def viewOnlineOrder(request):
	book_tb=BookModel.objects.filter(Status='online').order_by('-id')
	# print(delivery_tb)
	return render(request,'managerOnlineorderview.html',{'views':book_tb})


def staffAttendanceAction(request):
	date=request.POST['date']
	time=request.POST['time']
	manager=request.session['id']
	attendance_tb=AttendanceModel(Date=date,time=time,Manager_id=manager)
	attendance_tb.save()
	# staff_tb=StaffModel.objects.filter(Staff_id__in=id)
	present=request.POST.getlist('checkbox')
	print(present)
	for pid in present:
		if pid:

			status=PresentModel(Attendance=attendance_tb,Staff_id=pid,Status='Present')

		
			status.save()
	absent=StaffModel.objects.exclude(id__in=present)
	
	for ab in absent:
		print(ab.id)
		status=AbsentModel(Attendance=attendance_tb,Staff_id=ab.id,Status='Absent')
		status.save()
		print(absent)
		

	return redirect('staffAttendance')





def viewAttendance(request):
	present_tb=PresentModel.objects.all()
	absent_tb=AbsentModel.objects.all()
	return render(request,'viewattendance.html',{'views':present_tb,'absent':absent_tb})


def searchBydate(request):
	search=request.POST['date']
	present_tb=AttendanceModel.objects.filter(Date__istartswith=search,Status='Present')
	absent_tb=AttendanceModel.objects.filter(Date__istartswith=search,Status='Absent')
	return render(request,'viewattendance.html',{'views':present_tb,'absent':absent_tb})


def addtracking(request,id):
	delivery_tb=DeliveryModel.objects.filter(id=id)
	return redirect('viewOnlineOrder')


def addtrackingAction(request):
	order=request.POST['id']
	print(order)
	user=request.POST['userid']
	print(user)
	track=request.POST['tracking']
	print(track)
	delivery_tb=DeliveryModel.objects.filter(Order_id=order)
	delivery_tb.update(Tracking=track)
	print(delivery_tb)
	messages.add_message(request,messages.INFO,"Succesfully Added")

	return redirect('viewOnlineOrder')

def logout(request):
    request.session.clear()
    return redirect('/')
