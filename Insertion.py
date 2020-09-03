def insertionSort(arr): 
 
    for i in range(1, len(arr)): 
  	
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
arr = []  
n = int(input("Enter number of elements : ")) 
  
for i in range(0, n): 
    ele = int(input()) 
  
    arr.append(ele)
      
print("Your Data are :",arr) 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])

input('\nPress Enter to Exit...')




"""
#Output

Enter number of elements : 5
44
10
33
25
41
Your Data are : [44, 10, 33, 25, 41]
Sorted array is:
10
25
33
41
44
"""

