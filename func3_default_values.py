# WAPP to demonstrate arguments with default values in functions

def message(time, city, ampm = 'hrs'):
        str1 = "Time is "+ str(time) +ampm+" in "+city
        return str1

str2 = message(11, 'delhi', ' am')
print(str2)

str2 = message(20, 'delhi')
print(str2)

str2 = message(city='mumbai', time=2)
print(str2)

# def message(ampm = 'hrs', time, city ):
#parameters with default values must be in the end
