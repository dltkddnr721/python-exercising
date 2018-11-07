n= int(input())
m= int(input())
a = 4
b = 6
c = 12
d = 16
e = 20
f = 24
g = 28
h = 32
i = 36
w = [0,a,b,c,d,e,f,g,h,i]
q = w[n]&w[m]
p = w[n]|w[m]
o = list(bin(q))
iu= list(bin(p))
l = o.count("1")
u = int(iu.count("1"))
print(l)
print(u)
