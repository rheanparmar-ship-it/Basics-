'''c = 5
while c<21:
    print(c)
    c = c+1'''
#Even series
'''c=10
while c<41:
    print(c)
    c=c+1'''
#ODD SERIES
'''c=5
while c<41:
    print(c)
    c=c+2'''
#Reverse series
'''c=50
while c>24:
    print(c)
    c=c-1'''
#Validation of input
user="UID123"
password="Mentor25"
user_input=input("Enter username")
password_input=input("Enter password")
while user_input!=user and password_input!=password:
    print("Try again")
    user_input=input("Enter username")
    password_input=input("Enter password")
print("Access Granted")