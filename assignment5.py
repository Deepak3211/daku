#Q.1- Take an input year from user and decide whether it is a leap year or not. 
daku=int(input("Enter year you  want to  check:"))
if(daku%4==0 and daku%100!=0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.

length=int(input("Enter length:"))
breadth=int(input("Enter breadth:"))
if length==breadth:
    print("it is a square")
elif:
    print("it is a rectangle")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

a=int(input("Enter first age:"))
b=int(input("Enter second age:"))
c=int(input("Enter third age:"))
if a>=b and a>=c:
    print("oldest is:",a)
else:
    print("youngest is:",a)    
if b>=a and b>=c:
    print("oldest is:",b)
else:
    print("youngest is:",b) 
if c>=a and c>=b:
    print("oldest is:",c)
else:
    print("youngest is:",c)     
#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

#1. if employee is female, then she will work only in urban areas.
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#4. And any other input of age should print "ERROR"

age = int(input("Enter age"))
sex = input("SEX? (M or F)")
marry =input("MARRIED? (Y or N)")
if sex == "F" and age>=20 and age<=60:
  print ("Urban areas only")
elif sex == "M" and age>=20 and age<=40:
  print ("You can work anywhere")
elif sex == "M" and age>40 and age<=60:
  print ("Urban areas only")
else:
  print ("ERROR")
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter quantity"))
if quantity*100 > 1000:
  print ("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print ("Cost is",quantity*100)

  
#Q.6 Take 10 integers from user and print it on screen.

print(max([int(input("Enter a number: ")) for x in range(10)]))  


# Q.7 Write an infinite loop.An infinite loop never ends. Condition is always true. 
while True:
    print("Infinite")


#Q.8 From a list containing ints, strings and floats, make three lists to store them separately

dakuList = [ 4,'a', 'b', 'c', 1, 'd', 3,9.6,9.0]
from collections import defaultdict
d = defaultdict(list)
for x in dakuList:
   d[type(x)].append(x)

print( d[int])
print (d[str])
print(d[float])


#Q.9 Using range(1,101), make a list containing only prime numbers.

for num in range(1,101):
    if all(num%i!=0 for i in range(2,num)):
       print (num)
#Q.10- Print the following patterns:
*
**
***
****

def printSeriesIncreasing1(symbol,n):
	count=1
	while count<=n:
		print(symbol*count)
		count=count+1
	return
printSeriesIncreasing1('*',4)

#Q.11 Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

l = list(map(int,input("Enter list elements: ").split()))
element = int(input("Enter the element to search: "))
if element in l:
    print("Element found")
    del l[l.index(element)]
print(l)
    
    
    
