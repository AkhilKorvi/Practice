def three_sum_include_duplicates(nums):
    nums.sort()  # Step 1: Sort the list
    n = len(nums)
    triplets = []
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            
            elif total < 0:
                left += 1  # Need a larger sum, move the left pointer to the right
            else:
                right -= 1  # Need a smaller sum, move the right pointer to the left
    
    return triplets

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum_include_duplicates(nums)
print(result)


# OP : [[-1, -1, 2], [-1, 0, 1]]
