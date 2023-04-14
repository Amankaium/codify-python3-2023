class Bottle:
    def __init__(self, volume, color="white"):
        self.volume = volume
        self.color = color

    def __str__(self):
        return f"Баклашка {self.volume} {self.color}"


half = Bottle(color="red", volume=0.5) # call __init__
print(half.color)
print(half)
one = Bottle(1, "green")
cola = Bottle(2)
# cola.__init__(6)
