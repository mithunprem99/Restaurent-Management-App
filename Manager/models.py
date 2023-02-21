from django.db import models

# Create your models here.

class ManagerModel(models.Model):
	Name=models.CharField(max_length=255)
	Address=models.CharField(max_length=500)
	Gender=models.CharField(max_length=50,default='')
	DOB=models.CharField(max_length=50,default='')
	Phone=models.CharField(max_length=255)
	Email=models.EmailField(max_length=255)
	Username=models.CharField(max_length=255)
	Password=models.CharField(max_length=255)
	Image=models.FileField()
	Status=models.CharField(max_length=255,default='pending')


class FoodModel(models.Model):
	Food=models.CharField(max_length=255)
	Image=models.FileField()
	Price=models.CharField(max_length=50)
	Details=models.CharField(max_length=500)
	Category=models.CharField(max_length=500,default='')



class DinningModel(models.Model):
	Name=models.CharField(max_length=255)
	Chair=models.CharField(max_length=255,default='')
	Image=models.FileField(null=True)
	
	is_active=models.CharField(max_length=255,default='False')
	Booked_Status=models.CharField(max_length=255,default='pending')


# class DinningPlan(models.Model):
# 	Dinning=models.F
# 	Image=models.FileField(null=True)
	




class EventModel(models.Model):
	Name=models.CharField(max_length=255)
	Organizer=models.CharField(max_length=255)
	Date=models.CharField(max_length=255)
	Details=models.CharField(max_length=500)


class StockModel(models.Model):
	Item=models.CharField(max_length=255)
	Quantity=models.CharField(max_length=255)
	# Min_quantity=models.CharField(max_length=)


class AttendanceModel(models.Model):
	# Staff=models.ForeignKey('Admin.StaffModel',on_delete=models.CASCADE)
	Date=models.CharField(max_length=255,default='')
	time=models.CharField(max_length=255,default='')
	# Status=models.CharField(max_length=255,default='Absent')
	Manager=models.ForeignKey(ManagerModel,on_delete=models.CASCADE,null=True)
	

class PresentModel(models.Model):
	Attendance=models.ForeignKey(AttendanceModel,on_delete=models.CASCADE)
	Staff=models.ForeignKey('Admin.StaffModel',on_delete=models.CASCADE)

	Status=models.CharField(max_length=255)


class AbsentModel(models.Model):
	Attendance=models.ForeignKey(AttendanceModel,on_delete=models.CASCADE)
	Staff=models.ForeignKey('Admin.StaffModel',on_delete=models.CASCADE)

	Status=models.CharField(max_length=255)







