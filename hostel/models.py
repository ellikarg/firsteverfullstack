from django.db import models
from django.conf import settings


class Room(models.Model):
    rooms = (
        ('oia', 'OIÁ with 1 bed for 2 persons'),
        ('ogum', 'OGUM with 2 beds for 2 persons'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, choices=rooms)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.id} room {self.name} with {self.beds} bed(s) for {self.capacity} persons"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    class Meta:
        ordering = ['room', 'check_in']

    def __str__(self):
        return f"{self.user} has booked {self.room} from {self.check_in} until {self.check_out}"
