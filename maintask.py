# import random
# list1 = ['1','2','3','4','5','6','7','8','9','0']             1
# lucky_number1 = ""
# lucky_number2 = ""
# for i in range(0,10):
#     lucky_number1 += random.choice(list1)
#     lucky_number2 +=random.choice(list1)
# print(f"Lucky ticket is {lucky_number1}")
# print(f"Lucky ticket is {lucky_number2}")




# class Calculator:                         4
#     def __init__(self,number1,number2):
#         self.number1 = number1
#         self.number2 = number2
#     def addition(self):
#         return self.number1 + self.number2
#     def minus(self):
#         return self.number1 - self.number2
#     def multiplication(self):
#         return self.number1 * self.number2
#     def division(self):
#         return self.number1 / self.number2
#     def mod(self):
#         return self.number1 % self.number2
    
# number1 = int(input())
# char = input("-> ")
# number2 = int(input())

# calculator = Calculator(number1, number2)
# match char:
#     case '+':
#         result = calculator.addition()
#     case '-':
#         result = calculator.minus()
#     case '*':
#         result = calculator.multiplication()
#     case '/':
#         result = calculator.division()
#     case '%':
#         result = calculator.mod()    
#     case _:
#         print("not found")

# result = f"{number1} {char} {number2} = {result}"

    

# def Countdown(num):           3
#     while num > 0:
#         yield num 
#         num -= 1
# cd = Countdown(30)

# for x in cd:
#     if x % 7 == 0:
#         print(f"{x}")




# num = input().split(',')              2
# print(num)
# print(tuple(num))


# from datetime import datetime             5
# class Person:
#     def __init__(self,name,city,date_of_birth):
#         self.__name = name
#         self.__city = city
#         self.__date_of_birth = datetime.now().strftime('%m/%d/%Y')
#     def get_info(self):
#         return f"My name is :{self.__name}\n I live in :{self.__city}\n I am {self.__date_of_birth} years old"

# name = Person('Muhammad')
# city = Person('Tajikistan')
# birth = Person()



# def wrap(txt):            7
#     def wrapper():
#         print('Softclub')
#         txt()
#         print('W_Salom')
#     return wrapper
# @wrap 
# def main_func():
#     print('Salom akai Khayriddin')
# main_func()

# @helper('Salom ba shumo')
# def main_func():
#     print('Salom ba kursi Python')

# main_func()



num = input().split()
for i in num:
    
    print(list(i))

