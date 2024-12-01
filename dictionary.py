 
# dictionary it's mutable change
marks={
    "neetesh":99,
    "ram":45
}
print(marks)
print(marks["neetesh"])
print(marks.popitem()) #remove first items in marks
print(marks)

print(" pop method")
marks={
    "neetesh":99,
    "ram":45
}
print(marks.pop("neetesh", 99))
marks["ram"]=20
marks.update({"neetesh" : 80 , "manku": 50})                #add elements and also find "ram" = 45
print(marks)