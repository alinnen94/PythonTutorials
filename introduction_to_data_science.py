import math

# Operations
a = 1
# print(a)
b = 20/3
c = 20%3

# Error handling
for i in range(20):
    input_n = input("Input a number:")
    if input_n == "quit":
        break
    r = math.log(float(input_n))
    print(r)
