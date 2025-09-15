text=input("enter the line:")
words=text.split()
for word in list(words):
    print(word,words.count(word))

