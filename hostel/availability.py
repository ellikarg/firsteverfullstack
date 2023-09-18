import datetime
from hostel.models import Room, Booking

def check_availability(room, check_in, check_out):
    availability_list = []
    booking_list = Booking.objects.filter(room=room)

    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            availability_list.append(True)
        else:
            availability_list.append(False)
    return all(availability_list)
