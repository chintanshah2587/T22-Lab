# WAPP to demonstrate keyword arguments in functions

def message(time, ampm, city):
        str1 = "Time is "+ str(time) +ampm+" in "+city
        return str1

str2 = message(ampm=' pm', city='mumbai', time=2)
print(str2)

str2 = message(11, city='delhi', ampm=' am')
print(str2)

#str2 = message(city='delhi', ampm=' am', 11)
# Positional Arg cant follow Keyword Arg.
