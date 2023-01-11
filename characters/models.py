from django.db import models


class Character(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        GENDERLESS = "Genderless"
        UNKNOWN = "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    gender = models.CharField(choices=GenderChoices.choices, max_length=20)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name
