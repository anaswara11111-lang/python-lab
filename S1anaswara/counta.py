names = ["Alice", "Amanda", "Brian", "Carla", "David", "Angela"]
a_count = 0
for name in names:
    a_count += name.lower().count('a')
print("Total occurrences of 'a':", a_count)
