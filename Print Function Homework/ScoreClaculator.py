name = input("What is your name?")
math = int(input("What is your score in maths"))
english = int(input("What is your score in english"))
science = int(input("What is your score in science"))
total = math + english + science
percentage = total/3
percentage = round(percentage,2)
print(f"""
DETAILS
Name: {name}
Math score: {math}
English score: {english}
Science score: {science}
Total Cost: {total}
Percetage: {percentage}%
""")