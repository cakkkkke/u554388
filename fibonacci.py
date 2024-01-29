
def fibonacci_sequence(max_value):
    if max_value>1:
        fibonacci_sequence=[0,1]
        while fibonacci_sequence[-1] + fibonacci_sequence[-2]<=max_value:
            new_number=fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(new_number)
        print(fibonacci_sequence)
    elif max_value==1:
        fibonacci_sequence=[0,1]
        print(fibonacci_sequence)
    elif max_value==0:
        fibonacci_sequence=[0]
        print(fibonacci_sequence)
    else:
        print("error")

    

fibonacci_sequence(-1)
