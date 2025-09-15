text=input("enter the line:")
words=text.split()
for word in set(words):
    print(word,words.count(word))
