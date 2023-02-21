from django.db import models

# Create your models here.
class AdminModel(models.Model):
	Username=models.CharField(max_length=255)
	Password=models.CharField(max_length=255)


class StaffModel(models.Model):
	Name=models.CharField(max_length=255)
	Address=models.CharField(max_length=500)
	Gender=models.CharField(max_length=50)
	DOB=models.CharField(max_length=50)
	Phone=models.CharField(max_length=255)
	Email=models.EmailField(max_length=255)
	Image=models.FileField()
	Designation=models.CharField(max_length=255,default='')



class ReplayModel(models.Model):
	Complaint=models.ForeignKey('User.ComplaintModel',on_delete=models.CASCADE)
	Message=models.CharField(max_length=500)
	Status=models.CharField(max_length=255,default='pending')
	User=models.ForeignKey('User.UserModel',on_delete=models.CASCADE)