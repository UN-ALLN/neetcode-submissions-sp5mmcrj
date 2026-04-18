def add_two_numbers() -> int:
    

    two_int_input = input()

    #List of strings split by commas
    parsed_two_int_input = two_int_input.split(",")

    list_length = len(parsed_two_int_input)
    
    #each element is type casted to int
    for i in range(list_length):
        parsed_two_int_input[i] = int(parsed_two_int_input[i])
    
    #assign values from list to vars
    num_one = parsed_two_int_input[0]
    num_two = parsed_two_int_input[1]
    
    #add them together 
    sum = num_one + num_two

    return sum 


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
