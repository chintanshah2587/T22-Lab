# WAPP to demonstrate positional arguments in functions

def message(time, ampm, city):
        str1 = "Time is "+ str(time) +ampm+" in "+city
        return str1

str2 = message(2,'pm','mumbai')
print(str2)

str2 = message(11,'am','delhi')
print(str2)

#Fn Defn must come before Fn call
