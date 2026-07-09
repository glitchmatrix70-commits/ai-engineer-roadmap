# creating list and dict
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list.append(7)
my_dict['d'] = 4
my_list.extend([8, 9, 10])
print(my_list)
print(my_dict)

#for loop
for i in my_list:
    print(i)

for key, value in my_dict.items():
    print(f"{key}: {value}")

#while loop
count = 0
while count < 5:
    print(count)
    count += 1

#class
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

#creating object of class
s1=Student("Alice", 20, 85)
s1.display()

#functions
def add(a, b):
    return a + b

res = add(5, 10)
print(f"Sum: {res}")