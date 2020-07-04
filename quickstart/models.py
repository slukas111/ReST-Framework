from django.db import models
"""Joe's childhood in African Savanna is remembered by his statement
If you're not part of the solution, you're part of the precipitate"""


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style =models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = "R"
    ORANGE = "O"
    YELLOW = "Y"
    GREEN = "G"
    BLUE = "B"
    INDIGO = "I"
    VIOLET = "V"
    BLACK = "Bl"
    WHITE = "W"
    
    ROYGBIV = [
        ("R", "Red"),
        ("O", "Orange"),
        ("Y", "Yellow"),
        ("G", "Green"),
        ("B", "Blue"),
        ("I", "Indigo"),
        ("V", "Violet"),
        ("Bl", "Black"),
        ("W", "White"),
    ]
    shoe_color = models.CharField(max_length=2, choices=ROYGBIV, default=WHITE,)

    def __str__(self):
        return self.shoe_color


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name
