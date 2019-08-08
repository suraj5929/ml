import pandas as pd
n=int(input("enter the values"))
l = list(map(int,input().split()))
array=pd.Series(l)

print("mean:%f",array.mean())
print("median:%f",array.median())
print("mode:%f",array.mode())
print("sdanderd deviation:%f",array.std())
