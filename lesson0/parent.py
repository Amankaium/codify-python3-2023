# object
class Car: # предок
    color = "silver"  # attribute
    melee = 0  # attribute
    status = "ready"

    def go(self, km):  # method
        if self.status == "ready":
            print("Drdr")
            self.melee += km
            return "hello world"  # else None
        else:
            print("Break")


class Kamaz(Car):
    color = "grey"


class Rally(Kamaz): # потомок
    color = "blue"
    melee = 100000
    is_racing = True


r = Rally() # melee == 100000
r.go(33)
print(r.melee) # 100033
print(dir(r))