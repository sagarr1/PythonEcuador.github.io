# and operator

name = "sagar" 
age = 19
if name == "sagar" and age == 19:
    print("condition true")
else:
    print("condition false")    

# or operator 
if name == "sagar" or age == 34:
    print("condition true")
else:
    print("condition false") 

# exercise

#Bahubali 3
name = input("Enter your name :")
age = int(input("Enter your age:"))
if (name[0]=='a' or name[0]=='A') and age > 10:
    print("You can watch Bahubali 3 movie")
else:
    print("You can't watch Bahubali 3")   
