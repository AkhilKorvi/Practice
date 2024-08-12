MOD = 10**9 + 7

def get_expressions(num):
    n = len(num)
    total_sum = 0
    
    # There are 2^(n-1) ways to insert '+' between the digits
    for i in range(1 << (n - 1)):
        expression_sum = 0
        current_number = 0
        
        for j in range(n):
            current_number = current_number * 10 + int(num[j])
            
            # If the bit is set, or it's the last digit, add to the expression_sum
            if i & (1 << j) or j == n - 1:
                expression_sum += current_number
                current_number = 0
        
        total_sum = (total_sum + expression_sum) % MOD
    
    return total_sum

# Example usage:
print(get_expressions("123"))  # Expected output: 168
