

print("==============================================")
print("   Welcome to the Interactive Personal Data Collector!")
print("==============================================")


name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height in meters: "))

favorite_number = int(input("Please enter your favourite number: "))



current_year = 2026
birth_year = current_year - age



print("\nThank you! Here is the information we collected:\n")

print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Favourite Number:", favorite_number)



print("\n--- Data Types and Memory Addresses ---")

print("Name:")
print("  Type:", type(name))
print("  Memory Address:", id(name))

print("Age:")
print("  Type:", type(age))
print("  Memory Address:", id(age))

print("Height:")
print("  Type:", type(height))
print("  Memory Address:", id(height))

print("Favourite Number:")
print("  Type:", type(favorite_number))
print("  Memory Address:", id(favorite_number))



print("\nYour birth year is approximately:", birth_year)


print("\nThank you for using the Personal Data Collector. Goodbye!")
print("Keep exploring Python!")