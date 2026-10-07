


import math

# ej 1
def greet():
    print('Hello world')



# ej 2
def greet2(name):
    print(f'Hello {name}')



# ej 3
def pow(a, b):
    return a ** b

print(pow(6, 8))



# ej 4 
def celsius_to_fahrenheit(temperature):
    return temperature * 1.8 + 32

print(celsius_to_fahrenheit(23))



# ej 5
def area_circle(radius):
    return math.pi * radius ** 2

print(area_circle(7))



# ej 6
def avg(a, b, c):
    return (a + b + c) / 3

print(avg(9, 7, 10))



# ej 7 
def concat(a, b , c):
    return a + b + c

print(concat('Hola ', 'soy ', 'Nerea'))



# ej 8
def full_name(name, surname1, surname2):
    return name + " " + surname1 + " " + surname2

print(full_name('Nerea', 'Ros', 'Ocaña'))



# ej 9
def current_age(birth_year):
    return 2026 - birth_year

print(current_age(2001))



# ej 10
def introduction(name, surname1, surname2, birth_year):
    return (f"Hello I'm  {full_name(name, surname1, surname2)} and I'm {current_age(birth_year)}  years old")

print(introduction('Py', 'Thon', 'Rock', 1222))



# ej 11
def welcome():
    print('Welcome to this Python lesson')

welcome()



# ej 12
def welcome2(name):
    print(f'Hello {name}, wlcome to this Python lesson')

welcome2('Diego')



#ej 13
def double(number):
    return number * 2

print(double(6))



# ej 14
def price_with_tax(price):
    return price + price * 0.21



# ej 15
def price_with_tax(price, tax):
    return price + price * (tax / 100)



# ej 16
def volume_cube(side):
    return side ** 3



# ej 17
def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds



# ej 18
def pretty_text(text):
    return (f'=== {text} ===')



# ej 19
def format_name(name, surnames):
    return (f'{surnames}, {name}')



# ej 20 
def passed(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3 >= 5



# ej 21
def student_passed(name, surnames, grade1, grade2, grade3):
    return (f'{format_name(name, surnames)} has passed the subject: {passed(grade1, grade2, grade3)}')


