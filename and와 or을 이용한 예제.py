n=int(input())
m=int(input())
a = [0,0,0,1,0,0]
b = [0,0,1,0,0,0]
c = [0,0,1,1,0,0]
d = [0,1,0,0,0,0]
e = [0,1,0,1,0,0]
f = [0,1,1,0,0,0]
g = [0,1,1,1,0,0]
h = [1,0,0,0,0,0]
i = [1,0,0,1,0,0]
k = [a,b,c,d,e,f,g,h,i]
aa=k[n][0]*k[m][0]
bb=k[n][1]*k[m][1]
cc=k[n][2]*k[m][2]
dd=k[n][3]*k[m][3]
ee=k[n][4]*k[m][4]
ff=k[n][5]*k[m][5]
l=[aa,bb,cc,dd,ee,ff]
q=l.count(1)
print(q)
qq=k[n][0]|k[m][0]
ww=k[n][1]|k[m][1]
ee=k[n][2]|k[m][2]
rr=k[n][3]|k[m][3]
tt=k[n][4]|k[m][4]
yy=k[n][5]|k[m][5]
u=[qq,ww,ee,rr,tt,yy]
p=u.count(1)
print(p)



