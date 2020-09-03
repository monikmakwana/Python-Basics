#Create the multiplication table (from 1 to 10) of a number.
#Using while loop
no=int(input("Input a number : "))
cnt=1
while cnt<=10 :
    print(no,"*",cnt,"=",no*cnt) 
    cnt=cnt+1
input('\nPress Enter to Exit...')
