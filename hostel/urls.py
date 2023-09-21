from django.urls import path
from . import views
from .views import RoomListView, BookingList, BookingView, RoomDetailView

app_name = 'hostel'

urlpatterns = [
    path('', views.home, name='home'),
    path('academy/', views.academy, name='academy'),
    path('room_list/', views.RoomListView, name='room_list'),
    path('booking_list/', BookingList.as_view(), name='booking_list'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('room/<str:name>/', RoomDetailView.as_view(), name='room_detail_view'),
]
