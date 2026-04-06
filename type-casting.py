#input reading from user
name=input()
print(type(name),name)

#reading intergers from user
num=int(input())
print(type(num),num)

#reading float value from user
val=float(input())
print(type(val),val)

#reading the complex values
x=int(input())
y=int(input())
z=complex(x,y)
print(z)

#reading bollean values
n=bool(input())
#print(type(n),n)

#reading values from int to bollean
n=bool(int(input()))
print(type(n),n)

#id
a=257
b=257
c=30
print(id(a),id(b),id(c))
d=a+b+c
print(d)
