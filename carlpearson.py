
import cmath
l1=[15,12,8,8,7,7,7,6,5,3]

l2=[10,25,17,11,13,17,20,13,9,15]


avgl1=sum(l1)/len(l1)
avgl2=sum(l2)/len(l2)
for i in range(len(l1)):
    l1[i]-=avgl1

    

for i in range(len(l2)):
    l2[i]-=avgl2

l5=[]
for i in range(len(l1)):
    l5.append(l1[i]*l2[i])

l3=[]
for i in range(len(l1)):
    l3.append(l1[i]*l1[i])
sd1=cmath.sqrt(sum(l3)/len(l1))

l4=[]
for i in range(len(l2)):
    l4.append(l2[i]*l2[i])
sd2=cmath.sqrt(sum(l4)/len(l2))


r=(sum(l5)/10)/(sd1*sd2)
s=r.real
print(s)

