from django.db import models

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.id} room {self.name} with {self.beds} beds for {self.capacity} persons"
