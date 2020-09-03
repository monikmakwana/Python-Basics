# Input a number a check whether it is Prime or not
num = int(input("Enter Number to check whether it is Prime or not : "))
if num > 1:

    for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
    else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")
input('\nPress Enter to Exit...')

"""
Output:

Enter a number to check whether it is prime or not : 7
7 is a prime number

"""
