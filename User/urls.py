from django.urls import path,include
from .import views
# from User.views import Order

urlpatterns=[
	path('registerUser/',views.registerUser,name='registerUser'),
	path('logout/',views.logout,name='logout'),
	path('userRegisterAction/',views.userRegisterAction,name='userRegisterAction'),
	path('userHome/',views.userHome,name='userHome'),
	path('reserveAction/',views.reserveAction,name='reserveAction'),
	path('bookFood/<int:id>/',views.bookFood,name='bookFood'),
	path('bookFoodAction/',views.bookFoodAction,name='bookFoodAction'),
	path('breakfast/',views.breakfast,name='breakfast'),
	path('curry/',views.curry,name='curry'),
	path('lunch/',views.lunch,name='lunch'),
	path('drinks/',views.drinks,name='drinks'),
	path('snaks/',views.snaks,name='snaks'),
	path('getseat/',views.getseat,name='getseat'),
	path('cartView/',views.cartView,name='cartView'),
	path('deleteFromcart/<int:id>/',views.deleteFromcart,name='deleteFromcart'),
	path('placeOrder/',views.placeOrder,name='placeOrder'),
	path('viewOrder/',views.viewOrder,name='viewOrder'),
	path('cancelOrder/<int:id>/',views.cancelOrder,name='cancelOrder'),
	path('payNow/',views.payNow,name='payNow'),
	path('payNowAction/',views.payNowAction,name='payNowAction'),
	path('delivery/',views.delivery,name='delivery'),
	path('addFeedback/<int:id>/',views.addFeedback,name='addFeedback'),
	path('feedbackAction/',views.feedbackAction,name='feedbackAction'),
	path('viewFeedback/',views.viewFeedback,name='viewFeedback'),
	path('complaints/<int:id>/',views.complaints,name='complaints'),
	path('complaintAction/',views.complaintAction,name='complaintAction'),
	path('viewComplaints/',views.viewComplaints,name='viewComplaints'),
	path('viewreservation/',views.viewreservation,name='viewreservation'),
	path('cancelReserv/<int:id>/<int:tid>/',views.cancelReserv,name='cancelReserv'),
	path('edituser/',views.edituser,name='edituser'),
	path('usereditAction/',views.usereditAction,name='usereditAction'),
	path('checkUserName/',views.checkUserName,name='checkUserName'),
	path('getprice/',views.getprice,name='getprice'),
    path('getorder/',views.getorder,name='getorder'),
    path('getTable/',views.getTable,name='getTable'),
    path('viewMyOrder/<int:id>/',views.viewMyOrder,name='viewMyOrder'),
    path('getdinningImage/',views.getdinningImage,name='getdinningImage'),
    path("viewInbox",views.viewInbox,name='viewInbox'),
    path('changePassword/',views.changePassword,name='changePassword'),
    path('changePasswordAction/',views.changePasswordAction,name='changePasswordAction'),
    path('athome/',views.athome,name='athome'),
	path('viewOnline/<int:id>/',views.viewOnline,name='viewOnline'),
	path('onlineFeedback/<int:id>',views.onlineFeedback,name='onlineFeedback'),
	path('onlinefeedbackAction/',views.onlinefeedbackAction,name='onlinefeedbackAction'),
	path('onlineComplaints/<int:id>/',views.onlineComplaints,name='onlineComplaints'),
	path('trackmyOrder/<int:id>/',views.trackmyOrder,name='trackmyOrder'),
	path('paylater/<int:id>/',views.paylater,name='paylater')


    # path('Order/',Order.as_view())

	
	
	

]