#1.one egg price is 5 ruppees and what is price of 'N' eggs price
egg=5
n=int(input())
print(egg*n)

#2.if box contains N pencils and total price is M, then what price of each pencil price
m=int(input())
n=int(input())
print(m//n)

#3 red ball price is 25 green ball price is 30 if i buy n red balls and m -green balls than what is the total cost
red_balls=25
green_balls=30
x=int(input())
y=int(input())
print(x*red_balls+y*green_balls)

#4.check number is zero or non-zero
num=int(input())
if num==0:
    print("zero")
else:
    print("Non-zero")

#5.check number is +ve and -ve
number=int(input())
if  number >= 1:
    print("+ve")
else:
    print("-ve")

#6.check number is even or odd
num1=int(input())
if num1%2==0:
    print("even")
else:
    print("odd")

#7.check whether the person is eligible for vote or not
vote=int(input())
if vote>=18:
    print("eligible")
else:
    print("not eligible")

#8.check whether the number is divisible by 3 or not
num2=int(input())
if num2%3==0:
    print(f"{num2} is divisible by 3")
else:
    print("not divisible by 3")

#9.check whether the number is divisible by 3 and 5 or not
num3=int(input())
if num3%3==0 and num3%5==0:
    print(f"{num2} is divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#10.find bigger number amoung two number
firsno=int(input())
secdno=int(input())
if firsno>secdno:
    print(firsno)
else:
    print(secdno)

#11.grade Calcultor
marks=int(input())
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif  marks>=60 and marks<=79:
    print("C")
elif  marks>=40 and marks<=59:
    print("D")
else:
    print("invalid input")

# +ve odd,-ve odd,+ve even,-ve even
num=int(input())
if num>=0 and num%2==0:
    print("+ve even")
elif num<=-2 and num%2==0:
    print("-ve even")
elif num>=1 and num%2!=0:
    print("+ve odd")
else:
    print("-ve odd")

#using nested if 
num=int(input())
if num%2==0:
    if num>=0:
        print("+ve even")
    else:
        print("-ve even")
else:
    if num>=1:
        print("+ve odd")
    else:
        print("-ve odd")
