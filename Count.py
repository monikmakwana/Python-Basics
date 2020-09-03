def count(str): 
    vowels = 0
    consonant = 0
    lower = 0
    upper = 0
    for i in range(0, len(str)):            
        ch = str[i]    
        if ( (ch >= 'a' and ch <= 'z') or 
             (ch >= 'A' and ch <= 'Z') ):         
  
            if (ch == 'a' or ch == 'e' or ch == 'i' 
                or ch == 'o' or ch == 'u' or ch == 'A'
                or ch == 'E' or ch == 'I' or ch == 'O'
                or ch == 'U' ): 
                vowels += 1
            else: 
                consonant += 1
          
        if (ch >= 'a' and ch <= 'z'): 
            lower += 1
        if (ch >= 'A' and ch <= 'Z'): 
            upper += 1       
     
    print("Vowels:", vowels) 
    print("Consonant:", consonant)
    print("Uppercase:",upper)
    print("Lowercase:",lower)
  
str = input("Enter a String : ")
count(str)
input('\nPress Enter to Exit...')

"""
#Output

Enter a String : AEIOU iou zzz
Vowels: 8
Consonant: 3
Uppercase: 5
Lowercase: 6
"""
