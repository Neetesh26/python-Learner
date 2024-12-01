# String are immutable means it is not change  original string---->


name = "Neetesh_Prajapati"


nameSl = name[0:5]
print(nameSl)

print("good", name)

print(len(name))
# ******************* f string

print(f"good morning {name}")
print("good morning" + name)

# replace() chaning...
print(name.replace("Prajapati" , "mahakal"))

my = "hey my name is  there"
print( my.find("  "))