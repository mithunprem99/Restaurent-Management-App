from django.db import models

# Create your models here.

class UserModel(models.Model):
	Name=models.CharField(max_length=255)
	Address=models.CharField(max_length=500)
	Gender=models.CharField(max_length=50,)
	DOB=models.CharField(max_length=50)
	Phone=models.CharField(max_length=255)
	Email=models.EmailField(max_length=255)
	Username=models.CharField(max_length=255)
	Password=models.CharField(max_length=255)
	Image=models.FileField()


class Reservation(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	# Peoples=models.CharField(max_length=255,default='')
	
	Table=models.ForeignKey('Manager.DinningModel',on_delete=models.CASCADE,null=True)
	Date=models.CharField(max_length=255)
	Time=models.CharField(max_length=255)
	Food=models.ForeignKey('Manager.FoodModel',on_delete=models.CASCADE,null=True)
	Status=models.CharField(max_length=255,default='pending')
	


class CartModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Food=models.ForeignKey('Manager.FoodModel',on_delete=models.CASCADE)
	
	# Peoples=models.CharField(max_length=255,default='')
	Quantity=models.CharField(max_length=50,default='')
	Price=models.CharField(max_length=255)
	Total_Price=models.CharField(max_length=255,default='')

class BookModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Date=models.CharField(max_length=255)
	Time=models.CharField(max_length=255)
	Items=models.CharField(max_length=255,default='')
	Total_Price=models.CharField(max_length=255,default='')
	Payment_Status=models.CharField(max_length=255,default='pending')
	Status=models.CharField(max_length=255,default='pending')


class OrderModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Order=models.ForeignKey(BookModel,on_delete=models.CASCADE)
	Extra=models.CharField(max_length=25,default="",null=True)
	Table=models.ForeignKey('Manager.DinningModel',on_delete=models.CASCADE,null=True)
	Date=models.CharField(max_length=255,default='')
	Time=models.CharField(max_length=255,default='')
	Food=models.ForeignKey('Manager.FoodModel',on_delete=models.CASCADE)
	Status=models.CharField(max_length=255,default='pending')
	Payment_Status=models.CharField(max_length=255,default='pending')
	Quantity=models.CharField(max_length=50,default='')
	Total_Price=models.CharField(max_length=50,default='')
	Special_Request=models.CharField(max_length=500,default="",null=True)
	

class PaymentModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Order=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
	Card_Name=models.CharField(max_length=255)
	Card_Number=models.CharField(max_length=255)
	CVC=models.CharField(max_length=255)
	Exp_date=models.CharField(max_length=255)


class FeedbackModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Food=models.ForeignKey('Manager.FoodModel',on_delete=models.CASCADE)
	Date=models.CharField(max_length=255)
	Time=models.CharField(max_length=255)
	Feedback=models.CharField(max_length=500)


class ComplaintModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Food=models.ForeignKey('Manager.FoodModel',on_delete=models.CASCADE)
	Date=models.CharField(max_length=255)
	Time=models.CharField(max_length=255)
	Complaints=models.CharField(max_length=500)
	Status=models.CharField(max_length=255,default='pending')


class DeliveryModel(models.Model):
	User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
	Address=models.CharField(max_length=500,default='')
	Food=models.ForeignKey('Manager.FoodModel',on_delete=models.CASCADE)
	Quantity=models.CharField(max_length=255)
	Date=models.CharField(max_length=255)
	Time=models.CharField(max_length=255,null=True)
	Status=models.CharField(max_length=255,default='pending')
	Order=models.ForeignKey(BookModel,on_delete=models.CASCADE,default='')
	Total_Price=models.CharField(max_length=255,default='')
	Payment_Status=models.CharField(max_length=255,default='pending')
	Tracking=models.CharField(max_length=255,default='')



