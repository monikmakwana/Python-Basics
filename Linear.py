arr = []  
n = int(input("Enter number of elements : "))   
for i in range(0, n): 
    ele = int(input())   
    arr.append(ele)      
print("Your Data are :",arr)
item=int(input("Enter item to serach : "))
flat=0
for i in range(0,len(arr)):
    if(item==arr[i]):
        flag=1
        break
if(flag==1):
    print("Element found in index:",i)
else:
    print("Element not found")

input('\nPress Enter to Exit...')







"""
#Output

Enter number of elements : 5
10
20
30
40
50
Your Data are : [10, 20, 30, 40, 50]
Enter item to serach : 40
Element found in index: 3

"""
