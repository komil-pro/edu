a = 33
b = 33
if b > a:
  print("b больше a")
elif a == b:
  print("a и b равны")


i = 1
while i < 9:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


fruits = ["apple", "banana", "cherry"]
for x in range(len(fruits)):
  print(fruits[x])
  if fruits[x] == "banana":
    break
  

def my_function(firstname="Said",lastname="Rustamov"):
  print(firstname + " " + lastname)

my_function("Zebo", "Azizova")


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Suhrob", "Majidov")
#x.printname()

class Student(Person):
  kurs = 3

s1 = Student("Abdullo", "Zaripov")

s1.printname()
print(s1.kurs)

# lambda 
x = lambda a : a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))



class MyClass:
  x = 5


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

import datetime

x = datetime.datetime.now()
print(x)
