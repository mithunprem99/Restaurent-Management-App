from django.shortcuts import render,redirect
from Admin.models import*
from Manager.models import*
from User.models import *
from django.contrib import messages
# from reportlab.pdfgen import canvas  
from django.http import HttpResponse 
from django.http import JsonResponse
from datetime import datetime
# Create your views here.


def registerUser(request):
	return render(request,'userRegister.html')

def userRegisterAction(request):
	name=request.POST['name']
	address=request.POST['address']
	phone=request.POST['phone']
	gender=request.POST['gender']
	email=request.POST['email']
	dob=request.POST['dob']
	image=request.FILES.get('file')
	username=request.POST['username']
	password=request.POST['password']
	user_tb=UserModel(Name=name,Address=address,Phone=phone,Email=email,Image=image,Username=username,Password=password,Gender=gender,DOB=dob)
	user_tb.save()
	messages.add_message(request,messages.INFO,username+"Registrered Sucessfully")
	return render(request,'login.html')


def checkUserName(request):
	name=request.GET['uname']
	user_tb=UserModel.objects.filter(Username=name)
	if len(user_tb)>0:
		msg= "exist"
	else:
		msg="not exist"
	return JsonResponse({'valid':msg})


def userHome(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	# request.session['id']=user_tb[0].id
	# request.session['Username']=user_tb[0].Username

	# request.session['Name']=user_tb[0].Name
	feedback_tb=FeedbackModel.objects.all()
	return render(request,'userHome.html',{'views':food_tb,'events':event_tb,'table':table_tb,'feed':feedback_tb,'staff':staff_tb})

def breakfast(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	breakfast=FoodModel.objects.filter(Category='Breakfast')
	return render(request,'breakfast.html',{'break':breakfast,'views':food_tb,'events':event_tb,'table':table_tb,'staff':staff_tb})

def lunch(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	lunch=FoodModel.objects.filter(Category='Lunch')
	return render(request,'lunch.html',{'lunch':lunch,'views':food_tb,'events':event_tb,'table':table_tb,'staff':staff_tb})

def curry(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	curry=FoodModel.objects.filter(Category='Curry')
	return render(request,'curry.html',{'curry':curry,'views':food_tb,'events':event_tb,'table':table_tb,'staff':staff_tb})



def drinks(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	drinks=FoodModel.objects.filter(Category='Drinks')
	return render(request,'drinks.html',{'drinks':drinks,'views':food_tb,'events':event_tb,'table':table_tb,'staff':staff_tb})


def snaks(request):
	food_tb=FoodModel.objects.all()
	event_tb=EventModel.objects.all()
	table_tb=DinningModel.objects.filter(is_active='True')
	staff_tb=StaffModel.objects.filter(Designation='Chef')
	snaks=FoodModel.objects.filter(Category='Snack')
	return render(request,'snaks.html',{'snaks':snaks,'views':food_tb,'events':event_tb,'table':table_tb,'staff':staff_tb})




def reserveAction(request):
	user=request.session['id']
	# people=request.POST['people']
	tables=request.POST['tables']
	table=DinningModel.objects.get(id=tables)
	date=request.POST['date']
	time=request.POST['slot']
	reservation_tb=Reservation(Date=date,Time=time,User_id=user,Table=table)
	reservation_tb.save()
	
	dinning_tb=DinningModel.objects.filter(id=tables)
	# dinning_tb.update(Booked_Status='Booked')

	messages.add_message(request,messages.INFO,"Table Reserved")
	return redirect('userHome')


def bookFood(request,id):
	food=FoodModel.objects.filter(id=id)
	food_tb=FoodModel.objects.all()
	user=request.session['id']
	user_tb=UserModel.objects.filter(id=user)
	table=DinningModel.objects.filter(is_active='True')
	cart=CartModel.objects.filter(id=id)
	feedback_tb=FeedbackModel.objects.filter(Food_id=id)
	print(feedback_tb)
	return render(request,'addTocart.html',{'views':food,'user':user_tb,'din':table,'food':cart,'foods':food_tb,'feedback':feedback_tb})

def bookFoodAction(request):
	user=request.session['id']
	name=request.POST['name']
	item=request.POST['food']
	# date=request.POST['date']
	# time=request.POST['time']
	eat=FoodModel.objects.get(Food=item)
	price=request.POST['price']
	quantity=request.POST['quantity']
	# tables=request.POST['table']
	# table=DinningModel.objects.get(id=tables)
	total_price=request.POST['total']
	# people=request.POST['people']
	cart=CartModel(Price=price,Food=eat,User_id=user,Quantity=quantity,Total_Price=total_price)
	cart.save()
	
	messages.add_message(request,messages.INFO,"Item Added To cart Succesfully")
	cart_bt=CartModel.objects.filter(User_id=user)
	return redirect('userHome')


def cartView(request):
	user=request.session['id']
	cart_tb=CartModel.objects.filter(User=user)
	order_tb=OrderModel.objects.filter(Status='pending')
	table=DinningModel.objects.filter(is_active='True')
	user_tb=UserModel.objects.filter(id=user)
	return render(request,'cartview.html',{'view':cart_tb,'din':table,'user':user_tb})


def getdinningImage(request):
	table=request.GET['image']
	print(table)
	table_tb=DinningModel.objects.filter(id=table)
	print(table_tb)
	return render(request,'getImage.html',{'show':table_tb})



def getprice(request):
	fod=request.GET['eat']
	food_tb=FoodModel.objects.filter(id=fod)
	return render(request,'getprice.html',{'views':food_tb})



def deleteFromcart(request,id):
	cart_tb=CartModel.objects.filter(id=id).delete()
	
	return redirect('cartView')


def delivery(request):
	user=request.session['id']
	quantity=request.POST['quantity']
	print(quantity)
	order=request.POST.getlist('checkbox[]')
	# print(order)
	value=request.POST['amnt']
	# print(value)
	date=datetime.today().strftime("%Y-%m-%d")
	# print(date)
	item=len(order)
	# time=datetime.now().strftime('%H:%M:%S') 
	time=request.POST['slot']

	book=BookModel(Date=date,Time=time,User_id=user,Items=item,Total_Price=value,Status='online')
	book.save()
	address=request.POST['address']
	# status=book.Status
	# status.update(Status='online')
	for oid in order:
		cart=CartModel.objects.filter(id=oid)
		

		food=cart[0].Food_id


		# total=cart[0].Total_Price


		print(book.id)

		delivery_tb=DeliveryModel(Address=address,Order_id=book.id,User_id=user,Food_id=food,Date=date,Time=time,Quantity=quantity,Total_Price=value,Status='online')

	
		delivery_tb.save()
		cart.delete()

	

	return redirect('cartView')




def placeOrder(request):
	
	table=request.POST['table']
	print(table)
	value=request.POST['amnt']
	date=request.POST['date']
	time=request.POST['slot']
	quantity=request.POST['quantity']
	din=DinningModel.objects.get(id=table)
	print(din)
	order=request.POST.getlist('checkbox[]')
	spclrqst=request.POST['spclrqst']
	extra=request.POST['extra']
	item=len(order)
	user=request.session['id']
	book=BookModel(Date=date,Time=time,User_id=user,Items=item,Total_Price=value)
	book.save()
	# print(item)
	for oid in order:
		cart=CartModel.objects.filter(id=oid)
		

		food=cart[0].Food_id


		total=cart[0].Total_Price


		print(book.id)

		order_tb=OrderModel(Order_id=book.id,User_id=user,Table=din,Food_id=food,Date=date,Time=time,Quantity=quantity,Total_Price=total,Extra=extra,Special_Request=spclrqst)

		reservation=Reservation.objects.filter(id=oid)
		reservation=Reservation.objects.filter(User=user)
		reservation.update(Status='Booked')
		reservation_tb=Reservation(User_id=user,Food_id=food,Table=din,Date=date,Time=time)
		reservation=Reservation.objects.filter(User=user)
		reservation.update(Status='Booked')
		reserv=Reservation.objects.filter(id=oid)
		reserv.update(Status='Booked')
		reservation_tb.save()
		order_tb.save()
		cart.delete()

		table=DinningModel.objects.filter(id__in=table)
	


		messages.add_message(request,messages.INFO,"Table Reserved")




	return redirect('cartView')


def getorder(request):
	date=request.GET['date']
	time=request.GET['time']
	table=request.GET['table']

	date_tb=OrderModel.objects.filter(Date__istartswith=date,Time__istartswith=time,Table=table)

	if len(date_tb)>0:
		return JsonResponse({"name": "Failed"}, status=200)
	else:
		return JsonResponse({"name": "Success"}, status=200)
	


def getTable(request):
	date=request.GET['date']
	time=request.GET['time']
	table=request.GET['table']

	date_tb=Reservation.objects.filter(Date__istartswith=date,Time__istartswith=time,Table=table)
	# print(date_tb)
	if len(date_tb)>0:
		return JsonResponse({"name": "Failed"}, status=200)
	else:
		return JsonResponse({"name": "Success"}, status=200)




def viewOrder(request):
	user=request.session['id']
	book=BookModel.objects.filter(User=user).exclude(Status='online').order_by('-id')
	
	order_tb=OrderModel.objects.filter(User=user)

	return render(request,'viewMyorder.html',{'view':book})
	# else:
		# return render(request,'viewMyorder.html')

def athome(request):
	user=request.session['id']
	book=BookModel.objects.filter(User=user,Status='online').order_by('-id')

	order_tb=DeliveryModel.objects.filter(Order_id__in=book)

	return render(request,'atHome.html',{'view':book,'ord':order_tb})
	# else:
		# return render(request,'viewMyorder.html')






def cancelOrder(request,id):
	order_tb=BookModel.objects.filter(id=id)

	order_tb.delete()

	return redirect('viewOrder')

def viewOnline(request,id):

	book_tb=BookModel.objects.filter(id=id)
	print(book_tb)
	delivery_tb=DeliveryModel.objects.filter(Order_id__id=id).order_by('-id')
	print(delivery_tb)
	if (book_tb[0].id == delivery_tb[0].Order_id):
		# order=OrderModel.objects.filter(Order_id=id)
		# print(order)
		return render(request,'userOnlineView.html',{'view':delivery_tb,'pay':book_tb})

	else:
		return redirect('viewOrder')


def viewMyOrder(request,id):
	book_tb=BookModel.objects.filter(id=id)
	# print(book_tb)
	order_tb=OrderModel.objects.filter(Order_id__id=id).order_by('-id')
	# print(order_tb)
	if (book_tb[0].id == order_tb[0].Order_id):
		order=OrderModel.objects.filter(Order_id=id)
		# print(order)
		return render(request,'userOrderView.html',{'view':order_tb,'pay':book_tb})

	else:
		return redirect('viewOrder')




def payNow(request):
	# order_tb=OrderModel.objects.filter(id=id)
	# print(order_tb)
	
	order_tb=OrderModel.objects.filter(Order_id=pid)
	print(order_tb)
	return render(request,'paynow.html',{'views':order_tb})



def payNowAction(request):
	user=request.session['id']
	id=request.POST['id']
	name=request.POST['name']
	number=request.POST['number']
	exp=request.POST['exp']
	cvc=request.POST['cv']
	pay_tb=PaymentModel(Card_Name=name,Card_Number=number,Exp_date=exp,CVC=cvc,User_id=user,Order_id=id)
	pay_tb.save()
	order_tb=OrderModel.objects.filter(Order_id__id=id)
	delivery_tb=DeliveryModel.objects.filter(Order_id__id=id)

	book_tb=BookModel.objects.filter(id=id)
	order_tb.update(Payment_Status='Payment SuccessFull')
	delivery_tb.update(Payment_Status='Payment SuccessFull')

	book_tb.update(Payment_Status='Payment SuccessFull')
	messages.add_message(request,messages.INFO,"Payment Successfull")
	return redirect('viewOrder')


def trackmyOrder(request,id):
	book_tb=BookModel.objects.filter(id=id)
	delivery_tb=DeliveryModel.objects.filter(Order_id__in=book_tb)
	return render(request,'usertrackMyorder.html',{'views':book_tb,'food':delivery_tb})




	


def paylater(request,id):
	# cash=request.POST['id']
	print(id)
	book_tb=BookModel.objects.filter(id=id)
	print(book_tb)
	delivery_tb=DeliveryModel.objects.filter(Order_id=id)
	print(delivery_tb)
	delivery_tb.update(Payment_Status='on delivery')
	book_tb.update(Payment_Status='on delivery')
	return redirect('viewOrder')


# def ticket(request):
# 	user=request.session['id']
# 	order_tb=OrderModel.objects.filter(User=user)
# 	name=order_tb[0].User.Name
# 	order=order_tb[0].id
# 	print(order)
# 	response = HttpResponse(content_type='application/pdf')
# 	response['Content-Disposition'] = 'attachment; filename="file.pdf"'
# 	p = canvas.Canvas(response)
# 	p.setFont("Times-Roman", 15)
# 	p.drawString(100,700, "name,order")
# 	p.showPage()
# 	p.save()
# 	return response  


def addFeedback(request,id):
	order_tb=OrderModel.objects.filter(id=id)
	return render(request,'foodFeedback.html',{'views':order_tb})



def onlineFeedback(request,id):
	delivery_tb=DeliveryModel.objects.filter(id=id)
	return render(request,'onlinefeedback.html',{'views':delivery_tb})
		
def onlinefeedbackAction(request):
	user=request.session['id']
	food=request.POST['food']
	foodes=FoodModel.objects.get(Food=food)
	date=request.POST['date']
	time=request.POST['time']
	feedback=request.POST['feedback']
	feedback_tb=FeedbackModel(User_id=user,Food=foodes,Feedback=feedback,Date=date,Time=time)
	feedback_tb.save()
	messages.add_message(request,messages.INFO,"Thank You ☺ vist again have a nice day")

	return redirect('viewOrder')
def feedbackAction(request):
	user=request.session['id']
	food=request.POST['food']
	foodes=FoodModel.objects.get(Food=food)
	date=request.POST['date']
	time=request.POST['time']
	feedback=request.POST['feedback']
	feedback_tb=FeedbackModel(User_id=user,Food=foodes,Feedback=feedback,Date=date,Time=time)
	feedback_tb.save()
	messages.add_message(request,messages.INFO,"Thank You ☺ vist again have a nice day")

	return redirect('viewOrder')


def viewFeedback(request):
	user=request.session['id']
	feedback_tb=FeedbackModel.objects.filter(User_id=user)
	return render(request,'viewFeedback.html',{'views':feedback_tb})


def complaints(request,id):
	order_tb=OrderModel.objects.filter(id=id)
	return render(request,'complaints.html',{'views':order_tb})

def onlineComplaints(request,id):
	delivery_tb=DeliveryModel.objects.filter(id=id)
	return render(request,'Onlinecomplaints.html',{'views':delivery_tb})


def complaintAction(request):
	user=request.session['id']
	food=request.POST['food']
	foodes=FoodModel.objects.get(Food=food)
	date=request.POST['date']
	time=request.POST['time']
	complaint=request.POST['complaint']
	complaint_tb=ComplaintModel(User_id=user,Food=foodes,Complaints=complaint,Date=date,Time=time)
	complaint_tb.save()
	messages.add_message(request,messages.INFO,"Thank You ☺ and Sorry For the trouble")

	return redirect('viewOrder')


def viewComplaints(request):
	user=request.session['id']
	complaint_tb=ComplaintModel.objects.filter(User_id=user)
	return render(request,'viewComplaints.html',{'views':complaint_tb})


def viewreservation(request):
	user=request.session['id']
	reserv_tb=Reservation.objects.filter(User_id=user).order_by('-id')
	return render(request,'customerviewReservation.html',{'views':reserv_tb})


def cancelReserv(request,id,tid):
	reserv_tb=Reservation.objects.filter(id=id)
	reserv_tb.delete()
	tables=DinningModel.objects.filter(id=tid)
	tables.update(Booked_Status='pending')
	return redirect('viewreservation')


def edituser(request):
	user=request.session['id']
	user_tb=UserModel.objects.filter(id=user)
	return render(request,'userEdit.html',{'views':user_tb})


def usereditAction(request):
	id=request.POST['id']
	# user=request.session['id']
	user_tb=UserModel.objects.filter(id=id)
	name=request.POST['name']
	address=request.POST['address']
	phone=request.POST['phone']
	gender=request.POST['gender']
	email=request.POST['email']
	dob=request.POST['dob']
	username=request.POST['username']
	password=request.POST['password']
	if len(request.FILES)>0:
		file=request.FILES['file']
	else:
		file=user_tb[0].Image


	user_tb=UserModel.objects.filter(id=id).update(Name=name,Address=address,Phone=phone,Email=email,Username=username,Password=password,Gender=gender,DOB=dob)
	user_object=UserModel.objects.get(id=id)
	user_object.Image=file
	print(user_object.Image)
	user_object.save()
	messages.add_message(request,messages.INFO,"Updated Succesfully")
	return redirect('userHome')



def getseat(request):
	seat=request.GET['seats']
	dinning_tb=DinningModel.objects.filter(id=seat)
	return render(request,'getseat.html',{'seats':dinning_tb})

def viewInbox(request):
	user=request.session['id']
	print(user)
	replay_tb=ReplayModel.objects.filter(User_id__id=user)
	print(replay_tb)
	return render(request,'myinbox.html',{'view':replay_tb})


def changePassword(request):
	user=request.session['id']
	username=request.POST['username']
	email=request.POST['email']
	password=request.POST['password']
	user_tb=UserModel.objects.filter(Username=username,Email=email,Password=password)
	print(user_tb)
	if len(user_tb)>0:
		return render(request,'changeuserPassword.html',{'views':user_tb})

	else:
		return redirect('edituser')


def changePasswordAction(request):
	username=request.POST['username']
	password=request.POST['password']
	repass=request.POST['repass']
	if password == repass:
		user_tb=UserModel.objects.filter(Username=username)
		user_tb.update(Password=password)
		messages.add_message(request,messages.INFO,"Password Updated Succesfully")
		return redirect('edituser')
	else:
		messages.add_message(request,messages.INFO,"Password Not Match")
		return redirect('edituser')



# def addtrackingAction(request,id):


def logout(request):
    request.session.clear()
    return redirect('/')



