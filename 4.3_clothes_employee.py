# Exercise 1
clothes = ["socks", "shirt", "skirt", "scarf"]
def insert_element(new_cloth, index=0):

    return clothes.insert(index, new_cloth)

insert_element("t-shirt", 3)
print(clothes)
insert_element("t-shirt", -3)
print(clothes)
insert_element("t-shirt")
print(clothes)

# Exercise 2
employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
def replace_employee(old, new):

    x = employee_shift.index(old)
    employee_shift.remove(old)
    employee_shift.insert(x, new)

replace_employee('Kelly', "Maria")
print(employee_shift)