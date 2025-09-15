thislist=[3,1,4,9,8,2,6]
print("length of the list is:")
print(len(thislist))
print("enter last element:")
print(thislist[-1])
print("reverse of the list:")
print(thislist[::-1])
print(thislist)
print("9 is in this list or not:")
if 9 in thislist:
    print("yes 9 is in this list")
else:
    print("no 9 is not in this list")
print("add list")
thislist.insert(7,7)
print(thislist)
