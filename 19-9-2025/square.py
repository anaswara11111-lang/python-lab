n=int(input("enter a number"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
if n<=15:
    print(d)
else:
    print("nothing")
