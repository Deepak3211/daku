#Question 1
 x=['Python','Java','Ruby']
 x
#Question 2
x=['Python','Java','Ruby']
y=['c++','c','php']
x+y

#Question 3
x=['Deepak','Deepak','Rohan','Ayush']
x.count('Deepak')

#Question 4
x=['Deepak','Deepak','Rohan','Ayush']
x.sort()
x

#Question 5
x=['Deepak','Deepak','Rohan','Ayush']
x.sort()
x
y=['Surya','Rock','Punk','Akki']
y.sort()
y
x+y


#Question 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers:
if not x % 2:
count_even+=1
else:
count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#Question 7
def Reverse(tuples): 
    new_tup = tuples[::-1] 
    return new_tup
tuples = ('z','a','d','f','g','e','e','k') 
print(Reverse(tuples))

#Question 8
def daku(tuple):
length = len(tuple)
print("Largest element is:", tuple[length-1])
print("Smallest element is:", tuple[0])
tuple=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(tuple)

#Question 9
x='daku'
x.upper()

#Question 10
"9625657805".isdigit()

#Question 11
x='Hello World'
x.replace('World','Daku')

