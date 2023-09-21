from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Room, Booking
from .forms import BookingForm
from hostel.booking_functions.availability import check_availability


def home(request):
    return render(request, 'hostel/home.html')


def academy(request):
    return render(request, 'hostel/academy.html')


def RoomListView(request):
    return render(request, 'hostel/room_list.html')


class BookingList(ListView):
    model = Booking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff: 
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        rooms = self.kwargs.get('name', None)
        form = BookingForm()
        room_exists = Room.objects.filter(name=rooms).exists()
        if room_exists:
            room = Room.objects.get(name=rooms)
            room_name = room.name
            context = {
                'rooms': room_name,
                'form': form,
            }
            return render(request, 'hostel/room_detail_view.html', context)
        else:
            return HttpResponse('Room does not exist')

    def post(self, request, *args, **kwargs):
        rooms = self.kwargs.get('name', None)
        room_list = Room.objects.filter(name=rooms)
        form = BookingForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('Sorry, this room is already booked in the time you chose. Please try another room or date!')


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'hostel/booking_cancel_view.html'
    success_url = reverse_lazy('hostel:booking_list')