"""
Write a Python program which accepts a sequence of comma separated 4-digit binary numbers as
its input and print the numbers that are divisible by 5 in a comma separated sequence.
"""

print("Enter Sample Data : ")
data = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        data.append(p)
print(','.join(data))

input('\nPress Enter to Exit...')

"""
Output:

Enter Sample Data : 
0100,0011,1010,1001,1100,1001
1010

"""
