#QUES 1
a=int(input("enter a number "))
print(bin(a).replace("0b",""))

#QUES 2
a=int(input("input a no. "))
e=input("input the operator ")
b=int(input("input other no. "))

if e=="+":
    print(a+b)
elif e=="-":
    print(a-b)
elif e=="^":
    print(a**b)
elif e=="/":
    print(a/b)
elif e=="*":
    print(a*b)


#QUES 3
import math
#A
print((3+4)*(5))
#B
n=float(input("enter value of n "))
print((n*(n-1))/2)
#C
r=float(input("enter value of r "))
print(4*(math.pi)*r*r)
#D
a=int(input("enter value of a "))
b=int(input("enter value of b "))
r=int(input("enter value of r "))
c= math.radians(a)
h=math.radians(b)

print(math.sqrt(r*((((math.cos(c))**2))+(r*(((math.cos(c))**2))))))
#E
y1=int(input("enter value of y1 "))
y2=int(input("enter value of y2 "))
x1=int(input("enter value of x1 "))
x2=int(input("enter value of x2 "))
if x2==x1:
    print("invalid")
else:    
    print((y2-y1)/(x2-x1))
    
    
#QUES 4
x=range(5)
for n in x:
    print(n)
print("\n")

y=range(3,10)
for b in x:
    print(b)
print("\n")

z=range(4,13,3)
for c in x:
    print(c)
print("\n")

t=range(15,5,-2)
for d in x:
    print(d)
print("\n")

r=range(5,3)   
for e in x:
    print(e)
print("\n")


#QUES 5
h=int(input("enter number of hydrogen atoms "))
c=int(input("number of carbon atoms "))
o=int(input("number of oxygen atoms "))

mol_wt=(h*1.00794)+(c*12.0107)+(o*15.9994)
print("Molecular weight = ",mol_wt)