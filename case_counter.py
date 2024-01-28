
def case_counter():
    # Your code goes here
    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    # Delete this after implementing some code inside this function.
    text=input("Enter the text:")
    upper_counter=0;lower_counter=0
    for char in text:
        if char.isalpha():
            if char.isupper():
                upper_counter +=1
            elif char.islower():
                lower_counter+=1
            else:
                upper_counter += 0 ;lower_counter+=0                
        else:
            continue
    print("uppercase letter:",{upper_counter},", lowercase letter:",{lower_counter})




case_counter()

