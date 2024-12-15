### 1. Các thành phần cơ bản của Python
## 1.1. Hello World!
# print("Hello World!")

# if __name__ == '__main__': ## Chỉ được chạy code trên chính file này => file main
#     print("Hello World!")
    
## 1.2 Biến và Hằng số?  được định nghĩa giống nhau:
# number = 2
# print(number)

## 1.3 Kiểu dữ liệu: 
# var_int = 3
# var_float = 123.456 # || .0 || 12. 
# var_boolean = True # || False

# var_string = "Hello World"
# var_string2 = 'Hi'

# Xem kiểu dữ liệu của 1 biến: 
# print(type(var_float))

## 1.4 Phép toán : +, -, *, /, %, //. 
# So sánh: >, <, >=, <=, ==, !=
# Logic: AND & OR & 
# bool1 = 3 < 5 # True
# bool2 = 3 > 5 # False
# print("AND: ", bool1 and bool2) # 
# print("OR: ", bool1 or bool2) # 
# print("NOT: ",  not bool1) # 

# Input & Ouput: input(), print()
# var_input = input() # 4 => KDL: '4' => ép kiểu float/int(input())


## 1.5 Hàm (def): Thực hiện một nhiệm vụ cụ thể nào đó.
# def sum(a, b):
#     return a + b

# print(sum(2, 3)) # => 


## 1.6 Module: Code Python có thể được đóng gói thành module và được 
# sử dụng bởi các file Python khác. Các module sẵn có được gọi là thư viện 
# import math
# ## Pi = 180 độ
# print('sin: ', math.sin(math.pi/2)) # 1
# print('cos: ', math.cos(math.pi)) # -1


### 2. Cấu trúc điều kiện
## 2.1. Cấu trúc điều kiên
# num = 2.5
# if num == 2: 
#     print("This number is two")
# elif num==2.5:
#     print("This number is 2.5")
# else:
#     print("This number is not two")

## 2.2 Cấu trúc lặp: while, for .. in ..: lặp theo index, lặp theo giá trị
# name_arr = ['Khang', 'Long', 'Hung', 'Duc Anh']
# for i in range(0, len(name_arr)):
#     print(name_arr[i])
    
# for name in name_arr:
#     print(name)
    
## Sử dụng "break" để dùng vòng lặp
# for i in range(10):
#     print(i, end=" ")
#     if i>5: 
#         break

# i = 0 
# while i<10:
#     if i == 6:
#         i+= 1 # tăng 1 đơn vị mỗi lần lặp.
#         continue
#     print(i, end=" ")
#     i+= 1 # tăng 1 đơn vị mỗi lần lặp.


### 3. Lập trình hướng đối tượng OOP
"""
Python Là một ngôn ngữ lập trình hướng đối tượng. Nó cho phép lập trình viên
tạo ra các đối tượng trừu tượng nhằm làm cho code đơn giản, dễ đọc, dễ bảo trì.
"""

## 3.1 Lớp và đối tượng (class & object)
# class Person: 
#     race = "human" # class attribute
#     def __init__(self, name, age): # constructor
#         self.name = name           # Instance attribute
#         self.age = age
    
#     def say_hi(self):
#         print("Hello my name is " + self.name)
        
#     def tel_the_day(self, day):
#         print("Today is " + day)
        
# Khang = Person('Khang', 15)

# ## Gọi phương thức
# Khang.say_hi()
# Khang.tel_the_day("Sunday")

## 3.2 Thuộc tính (Attribute)
## Thuộc tính của lớp và thuộc tính của đối tượng
# Class Attribute
# print(Person.race) ## human

# Initialize object
# Long = Person("Long", 18)

# Get object attributes
# print("Age " + str(Long.age)) # 18 

# Set object attributes
# Long.age = 19
# print("Age " + str(Long.age)) # 19

#### Thuộc tính Public & Private
"""
Public attribute: thuộc tính có thể truy vấn tự do
Private attribute: thuộc tính chỉ được truy vấn bên trong class
"""

class Person: 
    race = "human" # class attribute
    def __init__(self, name, age): # constructor
        self.__name = name         # Private attribute
        self.age = age             # Public attribute
    
    def say_hi(self):
        print("Hello my name is " + self.__name)
    
    def getName(self):
        return self.__name
Hung = Person("Hung", 17)
print(Hung.age) ## 17

print(Hung.getName()) #