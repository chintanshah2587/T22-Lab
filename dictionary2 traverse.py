person1 = {'height': 5.5,  'weight': 65, 'eye_color': 'black'}
person2 = {'height': 5.8,  'weight': 75, 'eye_color': 'brown'}

for k in person1.keys():
    print(k)

print("=====================")

for v in person1.values():
    print(v)

print("=====================")

for Jack,Jill in person1.items():
    print(Jack , "-------" , Jill)

print("=====================")

for k in person2:
    print(k,"----",person2[k])

print("=====================")

for k in person1:
    print(k)

print("=====================")
