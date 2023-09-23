from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib import messages
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
        rooms = kwargs.get('name', None)
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
        rooms = kwargs.get('name', None)
        room_list = Room.objects.filter(name=rooms)
        form = BookingForm(request.POST)

        data = None

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        if data is not None:
            for room in room_list:
                if check_availability(room, data['check_in'], data['check_out']):
                    if data['check_in'] < data['check_out']:
                        available_rooms.append(room)
                    else:
                        messages.info(request, 'Your Check-out must be after your Check-in')
                        return redirect(request.get_full_path())
        if len(available_rooms) > 0:
            room = available_rooms[0]
            if request.user.is_authenticated:
                booking = Booking.objects.create(
                    user=self.request.user,
                    room=room,
                    check_in=data['check_in'],
                    check_out=data['check_out']
                )
                booking.save()
                messages.success(request, ('Thank you for your booking! You can find an overview of your bookings under "My Bookings".'))
                return render(request, 'hostel/room_list.html', {})
            else:
                messages.success(request, ('You have to be logged in to book a room.'))
                return render(request, 'account/login.html', {})
        else:
            messages.success(request, ('Sorry, this room is already booked in the time you chose. Please try another room or date!'))
            return redirect(request.get_full_path())


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'hostel/booking_cancel_view.html'
    success_url = reverse_lazy('hostel:booking_list')

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()

        messages.success(request, 'Your booking has been canceled!')

        return super().delete(request, *args, **kwargs)


class UpdateBookingView(UpdateView):
    model = Booking
    fields = ['check_in', 'check_out']
    template_name = 'hostel/update_booking_view.html'
    success_url = reverse_lazy('hostel:booking_list')

    def update(self, request, *args, **kwargs):
        booking = self.get_object()

        messages.success(request, 'Your booking has been updated!')

        return super().update(request, *args, **kwargs)
