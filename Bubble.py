def bubbleSort(arr): 
    n = len(arr) 
      
    for i in range(n-1): 
          
        for j in range(0, n-i-1): 
            
           if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = []  
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    arr.append(ele)      
print("Your Data are :",arr) 


bubbleSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  

input('\nPress Enter to Exit...')



"""
#Output

Enter number of elements : 3
20
10
30
Your Data are : [20, 10, 30]
Sorted array is:
10
20
30
"""

