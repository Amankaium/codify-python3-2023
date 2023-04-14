class Car:
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


mers = Car()
# print(mers.melee)  # 0
# mers.go(17)
# print(mers.melee)
# mers.go(250)
# print(mers.melee)
#
#
#
# print(mers.color)
# mers.color = "white"
# print(mers.color)
mers.status = "repair"
mers.go(6)


bmw = Car()
# print(bmw.color)
bmw.go(5)
