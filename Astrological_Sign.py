# Program to display astrological sign for a given date of birth.
def astrological_sign(day, month): 

    if month == 'december'.upper(): 
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
          
    elif month == 'january'.upper(): 
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
          
    elif month == 'february'.upper(): 
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
          
    elif month == 'march'.upper(): 
        astro_sign = 'Pisces' if (day < 21) else 'aries'
          
    elif month == 'april'.upper(): 
        astro_sign = 'Aries' if (day < 20) else 'taurus'
          
    elif month == 'may'.upper(): 
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
          
    elif month == 'june'.upper(): 
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
          
    elif month == 'july'.upper(): 
        astro_sign = 'Cancer' if (day < 23) else 'leo'
          
    elif month == 'august'.upper(): 
        astro_sign = 'Leo' if (day < 23) else 'virgo'
          
    elif month == 'september'.upper(): 
        astro_sign = 'Virgo' if (day < 23) else 'libra'
          
    elif month == 'october'.upper(): 
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
          
    elif month == 'november'.upper(): 
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
          
    print("Your Astrological sign is :",astro_sign) 
      
day = int(input("Input Day of birth : "))
m = input("Input Month of birth (in Words): ")
month=m.upper()
astrological_sign(day, month)
input('\nPress Enter to Exit...')
"""
Output:
input birthday : 15
input month of birth : May
Your Astrological sign is : Taurus

"""
