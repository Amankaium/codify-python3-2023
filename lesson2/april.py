from count import *

file_name = "april1"
april_budget = Budget(file_name)

comp_1 = Product("Lenovo", 500)
comp_2 = Product("HP", 1100)

comp_1.sell(file_name)
comp_2.sell(file_name)
comp_2.sell(file_name)
