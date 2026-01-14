# Write your code here
def create_dict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0]
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict
            
        
# HINT: create a dictionary from flowers.txt
flowers = create_dict('flowers.txt')
# HINT: create a function to ask for user's first and last name
def ask_name():
    name = input("Please enter your full name seperated by a space")
    first_name = name.split(" ")[0].upper()
    first_letter = first_name[0]
    return first_letter

first_letter = ask_name()
    
# print the desired output
print(f"Unique flower name with the first letter: {flowers[first_letter]}")
