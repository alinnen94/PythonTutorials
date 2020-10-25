import math
import time
import calendar
import numpy as np
import pandas as pd

# 2. Python
# Operations
a = 1
print(a)
b = 20/3
c = 20%3

# Error handling
for i in range(20):
    try:
        input_n = input("Input a number:")
        if input_n == "quit":
            break
        r = math.log(float(input_n))
        print(r)
    except ValueError:
        print("input error: value must be > 0")
    except Exception:
        print("Unknown error")

# Classes
class Person:
    energy = 1000
    def __init__(self, alias, age):
        self.alias = alias
        self.age = age
    def display_energy(self):
        print("Energy status is:", Person.energy)
    def display_alias(self):
        print(self.alias)

p_1 = Person("Alex", 26)
print(p_1.alias)
print(p_1.display_energy())

# Time module
print(time.time())
print(time.localtime())
print(calendar.month(2020, 9))

# Integer sort
l_1 = []
for i in range(3):
    input_n = int(input("Input number:"))
    l_1.append(input_n)
l_1.sort()
print(l_1)

# 3. Numpy
# Arrays
arr_1 = np.array([1, 2, 3, 4, 5, 6])
arr_1 += 1
print(arr_1)

# Matrices
m_1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(m_1)
print(m_1.shape)
print(m_1[1, 2])

# Need to use copy function to create new matrix based on another
m_2 = m_1.copy()
print(m_2)
n_3 = np.random.rand(10)
print(n_3)

# Mathematical functions
print(np.sum(n_3))
print(np.mean(n_3))
print(np.std(n_3))
print(np.round(n_3, decimals=2))

# Array functions
m_3 = np.ones(shape=(3,3))
print(m_3)
m_4 = np.zeros(shape=(3,3))
print(m_4)
m_5 = np.identity(6)
print(m_5)

# Random
print(np.random.rand(4,3))
print(np.random.randint(30, size=(5,6)))

# 4. Pandas
d_1 = {"Age": [20, 25, 30], "Height": [167, 170, 173]}
data_1 = pd.DataFrame(d_1)
print(data_1)
print(data_1.info)
print(data_1.describe())
