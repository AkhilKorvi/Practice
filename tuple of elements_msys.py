def merge_tuples(tuples_list):
    # Initialize the result list
    result = []
    
    # Iterate over the list with a step of 2
    for i in range(0, len(tuples_list), 2):
        # Get the first tuple in the pair
        first_tuple = tuples_list[i]
        # Get the second tuple in the pair
        second_tuple = tuples_list[i + 1]
        
        # Create a new tuple with the first element of the first tuple
        # and the second element of the second tuple
        new_tuple = (first_tuple[0], second_tuple[1])
        
        # Add the new tuple to the result list
        result.append(new_tuple)
    
    return result

# Example usage
L = [(2, 3), (4, 5), (9, 11), (12, 15)]
result = merge_tuples(L)
print(result)
