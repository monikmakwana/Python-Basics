def isPalindrome(str): 
    return str == str[::-1] 
    
str = input("Enter String to check it is Palindrome or not : ")
ans = isPalindrome(str) 
  
if ans: 
    print("Yes it is Palindrome") 
else: 
    print("No it is not Palindrome") 
input('\nPress Enter to Exit...')
"""
#Output

Enter String to check it is Palindrome or not : nayan
Yes it is Palindrome
"""
