from django.urls import path,include
from .import views

urlpatterns=[

	# path('managerRegister/',views.managerRegister,name='managerRegister'),
    # path('managerRegisterAction/',views.managerRegisterAction,name='managerRegisterAction'),
    path('addFood/',views.addFood,name='addFood'),
    path('addFoodAction/',views.addFoodAction,name='addFoodAction'),
    path('viewFood/',views.viewFood,name='viewFood'),
    path('updateFood/<int:id>/',views.updateFood,name='updateFood'),
    path('updateFoodAction/',views.updateFoodAction,name='updateFoodAction'),
    path('deleteFood/<int:id>/',views.deleteFood,name='deleteFood'),
    path('dinningTables/',views.dinningTables,name='dinningTables'),
    path('dinningTablesAction/',views.dinningTablesAction,name='dinningTablesAction'),
    path('deleteTable/<int:id>/',views.deleteTable,name='deleteTable'),
    path('dinningActivateAction/',views.dinningActivateAction,name='dinningActivateAction'),
    path('addEvents/',views.addEvents,name='addEvents'),

    path('addEventsAction/',views.addEventsAction,name='addEventsAction'),
    path('eventManage/',views.eventManage,name='eventManage'),
    path('updateEvent/<int:id>',views.updateEvent,name='updateEvent'),
    path('updateEventAction/',views.updateEventAction,name='updateEventAction'),
    path('deleteEvent/<int:id>/',views.deleteEvent,name='deleteEvent'),
    path('viewFoodOrder/',views.viewFoodOrder,name='viewFoodOrder'),
    path('confirmOrder/<int:id>/',views.confirmOrder,name='confirmOrder'),
    path('reservation/',views.reservation,name='reservation'),
    path('adminMessage/',views.adminMessage,name='adminMessage'),
    path('viewConfirmedOrder/',views.viewConfirmedOrder,name='viewConfirmedOrder'),
    path('viewOnlineOrder/',views.viewOnlineOrder,name='viewOnlineOrder'),
    path('addtracking/<int:id>/',views.addtracking,name='addtracking'),
    path('addStock/',views.addStock,name='addStock'),
    path('addStockAction/',views.addStockAction,name='addStockAction'),
    path('Stockupdate/<int:id>/',views.Stockupdate,name='Stockupdate'),
    path('StockupdateAction/',views.StockupdateAction,name='StockupdateAction'),
    path('deleteStock/<int:id>',views.deleteStock,name='deleteStock'),
    path('staffAttendance/',views.staffAttendance,name='staffAttendance'),
    path('staffAttendanceAction/',views.staffAttendanceAction,name='staffAttendanceAction'),
    path('viewAttendance/',views.viewAttendance,name='viewAttendance'),
    path('searchBydate/',views.searchBydate,name='searchBydate'),
    path('logout/',views.logout,name='logout'),
    path('addtrackingAction/',views.addtrackingAction,name='addtrackingAction'),
]