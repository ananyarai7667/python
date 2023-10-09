def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18:
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()


#compare age to 18 in the condition age >= 18,
# we're comparing a string (age) to an integer (18). 
# This will result in a TypeError because 
# cannot directly compare these two types