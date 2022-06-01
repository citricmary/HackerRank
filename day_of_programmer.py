def dayOfProgrammer(year):

    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            date = "12.09." + str(year)           
        else: 
            date = "13.09." + str(year) 

    if year > 1918 and year <= 2700:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            date = "12.09." + str(year) 
        else:
            date = "13.09." + str(year)

    if year == 1918:
        date = "26.09." + str(year)
    
    return date



print(dayOfProgrammer(2017))




