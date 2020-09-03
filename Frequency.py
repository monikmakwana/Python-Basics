def count(elements): 
    if elements[-1] == '.': 
        elements = elements[0:len(elements) - 1]  

    if elements in dictionary: 
        dictionary[elements] += 1
    else: 
        dictionary.update({elements: 1})    
   
Sentence = input("Enter String : ")   
dictionary = {}    
lst = Sentence.split()    
for elements in lst: 
    count(elements) 
    
for allKeys in dictionary: 
    print ("Frequency of", allKeys, end = " ") 
    print (":", end = " ") 
    print (dictionary[allKeys], end = " ") 
    print()
	input('\nPress Enter to Exit...')

"""
#Output

Enter String : Monik Monik Makwana
Frequency of Monik : 2 
Frequency of Makwana : 1
"""
