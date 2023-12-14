from django.db import models


class Airport(models.Model):
    name = models.TextField()
    closest_big_city = models.TextField()

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='source_routes')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_routes')
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.source} - {self.destination}. Distance: {self.distance}"
