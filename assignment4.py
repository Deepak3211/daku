#Q.1- Reverse the whole list using list methods. 
list=[20,30,90,'daku','game','c++',70,80]
list.reverse()
print(list)

#Q.2- Print all the uppercase letters from a string. 
d="My Name is Daku"
for i in d:
    if i==i.upper():
        print(i,end="|")

#Q.3- Split the user input on comma's and store the values in a list as integers.

lst1=list(input("Enter the elements: ").split(","))
print(lst1)



#Q.4- Check whether a string is palindromic or not.

d=input("Enter a string")
if a[::-1]==d:
    print("It is a palindrome")

else:
    print("It is not a palindrome")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
#shallow copy
lst2=[2,5,7]
lst3=lst
print("original list: ",lst2,"id=",id(lst2))
print("shallow copy list : ",lst2,"id=",id(lst3))

#deep copy
lst12=lst2.copy()
print("original list: ",lst2,"id=",id(lst2))
print("deep copy list: ",lst12,"id=",id(lst12))
    
    
        

    

