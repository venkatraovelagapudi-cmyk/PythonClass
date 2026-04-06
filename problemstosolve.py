#1.Write a program to add two numbers and print the result.
a=int(input())
b=int(input())
print(a+b)

#2.Take two integers as input and print their quotient and remainder.
x=int(input())
y=int(input())
print(x/y)
print(x%y)

#3.Given a number, check if it is even or odd using the modulus operator.
num=int(input())
if num%2==0:
    print("even")
else:
    print("odd")

#4.Write a program to swap two variables using arithmetic operators (without a third variable).
a,b=20,50
a,b=b,a
print(a,b)

#5.Take three numbers and print the largest using comparison operators.
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(num1)
elif num2>num3:
    print(num2)
else:
    print(num3)

#6.Write a program to calculate the square of a number using the exponent operator (**).
sqrt=int(input())
print(sqrt**2)

#7.Given two numbers, check if the first is divisible by the second.
firstno=int(input())
secdno=int(input())
if secdno%firstno==0:
    print(f"{firstno} is divisible by {secdno}")
else:
    print("not divisible")

#8.Write a program to calculate the area of a rectangle using multiplication operator.
length=int(input())
width=int(input())
area=length*width
print(f"area of a rectangle={area}")

#9.Take a number and print whether it is positive, negative, or zero.
number=int(input())
if number==0:
    print("zero")
elif num>=1:
    print("positive")
else:
    print("negative")

#10.Write a program to check if two numbers are equal using the equality operator (==).
numb1=int(input())
numb2=int(input())
if numb1==numb2:
    print("equal")
else:
    print("not equal")

#11.Write a program to check if a person is eligible to vote (age ≥ 18).
vote=int(input())
if vote>=18:
    print("eligible")
else:
    print("not eligible")

#12.Take a number and check if it is a multiple of both 3 and 5.
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("It is a multiple of both 3 and 5")
else:
    print("It is NOT a multiple of both 3 and 5")

#13.Write a program to find the greatest of three numbers using nested if.
number1=int(input())
number2=int(input())
number3=int(input())
if number1>number2:
    if  number1>number3:
        print(number1)
    else:
        print(number3)
else:
    if number2>number3:
        print(number2)
    else:
        print(number3)

#14.Given a year, check if it is a leap year. Write a program to classify a character as vowel or consonant.
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not leap year")

#15.Take marks as input and print grade according to conditions:
"""≥90 → A
75–89 → B
50–74 → C
<50 → Fail"""
marks=int(input())
if marks>=90:
    print("A")
elif 75<=marks<=89:
    print("B")
elif 50<=marks<=74:
    print("C")
else:
    print("Fail")

#16.Write a program to check if a number is prime.
prime=int(input())
if prime<=1:
    print("not prime")
else:
    for i in range(2,prime+1):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")

#17.Take a number and check if it is a palindrome.
palim = int(input())
temp = palim
rev = 0
while palim > 0:
    lastdigit = palim % 10
    rev = rev * 10 + lastdigit
    palim = palim // 10
if rev==temp:
    print("palindrome")
else:
    print("not palindrome.")

#18.Write a program to calculate electricity bill: Up to 100 units → ₹5/unit 101–200 units → ₹7/unit Above 200 units → ₹10/unit
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity Bill =", bill)

#19.Write a program to check if a given year is a century year (ends with 00) and also if it is a leap century
year = int(input("Enter year: "))

if year % 100 == 0:
    print("Century Year")
    
    if year % 400 == 0:
        print("Leap Century")
    else:
        print("Not a Leap Century")
else:
    print("Not a Century Year")
