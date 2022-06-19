a,b=map(int,input().split())
a=(a+(b-45)//60)%24
b=(b-45)%60
print(a,b)
#print((10 + (10 - 45) // 60) % 24)
#print(-35 // 60)