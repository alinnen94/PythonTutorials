import math
import time
import calendar

# # Operations
# a = 1
# print(a)
# b = 20/3
# c = 20%3
#
# # Error handling
# for i in range(20):
#     try:
#         input_n = input("Input a number:")
#         if input_n == "quit":
#             break
#         r = math.log(float(input_n))
#         print(r)
#     except ValueError:
#         print("input error: value must be > 0")
#     except Exception:
#         print("Unknown error")
#
# # Classes
# class Person:
#     energy = 1000
#     def __init__(self, alias, age):
#         self.alias = alias
#         self.age = age
#     def display_energy(self):
#         print("Energy status is:", Person.energy)
#     def display_alias(self):
#         print(self.alias)
#
# p_1 = Person("Alex", 26)
# print(p_1.alias)
# print(p_1.display_energy())
#
# # Time module
# print(time.time())
# print(time.localtime())
# print(calendar.month(2020, 9))

# Integer sort
l_1 = []
for i in range(3):
    input_n = int(input("Input number:"))
    l_1.append(input_n)
l_1.sort()
print(l_1)

