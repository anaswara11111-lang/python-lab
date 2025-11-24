def fibonacci_series(n):
    series=[]
    a,b = 0,1
    for _ in range(n):
        series.append(a)
        print(a,end=" ")
        a,b = b,a + b
    return series
