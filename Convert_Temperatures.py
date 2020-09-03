#Program to convert temperatures to and from Celsius, Fahrenheit.

C=int(input("Enter temperature in Celsius : "))
F=int(input("Enter temperature in Fahrenhit : "))
toF=(9*C/5)+32
toC=((F-32)*5)/9
print(C,"°C is",int(toF),"in Fahrenhit")
print(F,"°F is",int(toC),"in Celsius")
input('\nPress Enter to Exit...')

"""
Output:

Enter temperature in Celsius : 60
Enter temperature in Fahrenhit : 45
60 °C is 140 in Fahrenhit
45 °F is 7 in Celsius

"""
