from django.urls import path,include
from .import views

urlpatterns=[
	path('',views.index,),
    path('login/',views.login,name='login'),
    path('loginAction/',views.loginAction,name='loginAction'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('addManager/',views.addManager,name='addManager'),
    path('addmanagerAction/',views.addmanagerAction,name='addmanagerAction'),
    path('adminmanagerView/',views.adminmanagerView,name='adminmanagerView'),
    path('editManager/<int:id>/',views.editManager,name='editManager'),
    path('managerUpdateAction/',views.managerUpdateAction,name='managerUpdateAction'),
    path('deleteManager/<int:id>/',views.deleteManager,name='deleteManager'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('addstaffAction/',views.addstaffAction,name='addstaffAction'),
    path('viewStaff/',views.viewStaff,name='viewStaff'),
    path('staffupdate/<int:id>/',views.staffupdate,name='staffupdate'),
    path('staffupdateAction/',views.staffupdateAction,name='staffupdateAction'),
    path('staffdelete/',views.staffdelete,name='staffdelete'),
	path('staffdelete/<int:id>/',views.staffdelete,name='staffdelete'),
    path('viewCustomerfood/',views.viewCustomerfood,name='viewCustomerfood'),
    path('viewReservations/',views.viewReservations,name='viewReservations'),
    path('adminviewAttendance/',views.adminviewAttendance,name='adminviewAttendance'),
    path('adminsearchBydate/',views.adminsearchBydate,name='adminsearchBydate'),
    path('feedbacks/',views.feedbacks,name='feedbacks'),
    path('viewcomplaints/',views.viewcomplaints,name='viewcomplaints'),
    path('checkMUserName/',views.checkMUserName,name='checkMUserName'),
    path('adminsearchOrderBydate/',views.adminsearchOrderBydate,name='adminsearchOrderBydate'),
    path('adminsearchReservationBydate/',views.adminsearchReservationBydate,name='adminsearchReservationBydate'),
    path('forgotpasswordone/',views.forgotpasswordone,name='forgotpasswordone'),
    path('forgotpasswordoneAction/',views.forgotpasswordoneAction,name='forgotpasswordoneAction'),
    path('newpasswordAction/',views.newpasswordAction,name='newpasswordAction'),
    path('checkUserName/',views.checkUserName,name='checkUserName'),
    path('msgforward/<int:id>/',views.msgforward,name='msgforward'),
    path('replayComplaints/<int:id>/',views.replayComplaints,name='replayComplaints'),
    path('replayComplaintsAction/',views.replayComplaintsAction,name='replayComplaintsAction'),
    path('viewOnlineCustomerfood/',views.viewOnlineCustomerfood,name='viewOnlineCustomerfood')

	
]