li1=[10,30,40,58,23,7]
li2=[21,78,90,9,45,23,12,43]
print(len(li1))
print(len(li2))
if len(li1)==len(li2):
     print("The lists are of same length")
else:
    print("The lists are not same length")
print(sum(li1))
print(sum(li2))
if sum(li1)==sum(li2):
    print("sums are same")
else:
    print("sums are not same")

if any(value in li2 for value in li1):
    print("There is at least one common value.")
else:
    print("No common values found.")
common_values=[]
for item in li1:
    if item in li2 and item not in common_values:
        common_values.append(item)
print("common_values:",common_values)
