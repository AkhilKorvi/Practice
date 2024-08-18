#ip = 'abaccdcc'
#list of substring of palindrome from string
def palindrome(ip):
    n = len(ip)
    count = 0
    palindromes = []
    
    for i in range(n):
        for j in range(i+1,n+1):
            substr = ip[i:j]
            if is_palindrome(substr):
                palindromes.append(substr)
                
    return palindromes
    
def is_palindrome(s):
    return s == s[::-1]
    
ip = 'abaccdcc'
result = palindrome(ip)
print(result)
#for i in range(0 , len(result)):
#    print(result[i])
