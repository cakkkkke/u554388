number = 42
converted_to_string = str(number)
print(f"Number {converted_to_string} is now a string.")
print(type(converted_to_string))
# Output: Number 42 is now a string.
# <class 'str'>

float_number = 3.6
converted_to_int = int(float_number)
print(f"Float {float_number} is converted to integer {converted_to_int}.")
print(type(converted_to_int))



fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # This line is part of the for loop
    print(fruit , " is delicious!")  # This line is also part of the for loop


for fruit in fruits:
    print(fruit)  # This line is part of the for loop

print("All fruits have been printed.")  # This line is NOT part of the for loop


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Incorrect: Missing colon at the end of the 'for' statement

    
my_list = [1, "Hello", 3.14]
print(my_list)  # Output: [1, 'Hello', 3.14]
print(my_list[0])   # Output: 1 (first item)
print(my_list[1])   # Output: "Hello" (second item)
