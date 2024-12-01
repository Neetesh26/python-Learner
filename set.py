# immutable  not change
# empty set
n = set()

# in set have no index value
# set is never print duplicate value
# set is not repeate any values ,  also it is not sorted 
s = {1,2,3,4,56,3,3,56,1,"neetesh"}
s.add(2626) #add method
print(s)
print(s.pop())  #first value remove or random elem remove 
print(s)
s.remove(4)
print(s)

# print(s.pop())
s1 ={6,5,9,8,}
s2 ={8,6,4,2}
print(s1.union(s2))
print(s1.intersection(s2))