a=10;b=20
print("Arthematic Operators")
print('-'*25)
print(f"Addition of {a,b}={a+b}\n",
      f"Subtraction of {a,b}={a-b}\n",
      f"Multiplication of {a,b}={a*b}\n",
      f"Division of {a,b}={a/b}\n",
      f"Modulus of {a,b}={a%b}\n",
      f"Floor Division of {a,b}={a//b}\n",
      f"Exponent of {a,b}={a**b}\n")
print("Assignment  Operators")
print('-'*25)
z=25;x=20;y=39;p=34;l=56;s=43;t=32
z+=2;x-=32;y*=23;p%=36;l/=90;s//=65;t**=2
print(f"Addition assignment:{z}\n"
      f"Subtraction assignment:{x}\n"
      f"AMultiplication assignment:{y}\n"
      f"Modular assignment:{p}\n"
      f"Division assignment:{l}\n"
      f"Floor division assignment:{s}\n"
      f"Exponent assignment:{t}\n")
print("Relational  Operators")
print('-'*25)
print(f"Greaterthan {a}>{b}:{a>b}\n"
      f"lessrthan {a}<{b}:{a<b}\n"
      f"Greaterthan or Equalto {a}>={b}:{a>=b}\n"
      f"Lesserthan or Equal to {a}<={b}:{a<=b}\n"
      f"Equalto{a}=={b}:{a==b}\n"
      f"Not Equalto {a}!={b}:{a!=b}\n")
print("Relational  Operators")
print('-'*25)
print(f"LogicalAnd :- 10<20 and 10>11 : {10<20 and 10>11}\n"
      f"LogicalAnd :- 1 and 0 : {1 and 0}\n"
      f"LogicalAnd :- 10 and 5: {10 and 5}\n"
      f"Logicalor :- 10!=20 or 10>11 : {10!=20 or 10}\n"
      f"Logicalor  :- 0 or 10>11 : {0 or 10}\n"
     #f"Logicalnot :- not false: {not false}\n"
      )
print("Bitwise Operators")
print('-'*25) 
print(f"BitwiseAnd :- 10&11 : {10 & 11}\n"
      f"Bitwiseor :- 10 ^ 12 : {10 ^ 12}\n"
      f"Leftshift :- 20<<2 : {20<<2}\n"
      f"rightshift :- 10>>2: {10>>2}\n"
      f"OR(|)        :- 10 | 11  : {10 | 11}\n"
      f"NOT  (~)      :- ~10      : {~10}\n"
      )
print("Identity  Operators")
print('-'*25) 
print(f"is => a is b : {a is b}\n"
      f"is not => a is not b : {a is not b}\n"
      )
print("Membership Operators")
print('-'*25) 
print(f"is => 5 in [1,2,3,4] : {5 in [1,2,3,4]}\n"
      f"is not => 'z' not in 'srinu' : {'z' not in 'srinu'}\n"
      )
