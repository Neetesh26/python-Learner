# it is a immutable means it is not change  (similar type of list but it is not change original (immutable not change))

#empty tuple 
a =()
print(type(a))

b = (2,6,54,58,99,88,4,"np")

print(b.index(58))

repeated = b *2  # repeated no of times of values it is tuples
print(repeated)
print(len(repeated))



marks =[]
f1 = int(input("enter val..."))
marks.append(f1)
f2 = int(input("enter val..."))
marks.append(f2)
f3 = int(input("enter val..."))
marks.append(f3)
f4 = int(input("enter val..."))
marks.append(f4)
marks.sort()
print(marks)