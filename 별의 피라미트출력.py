print "A-1"
print "*"
print "**"
print "***"
print "****"
print "*****"
print""
print""
print"A-2"
print "**********".center(30)
print "********".center(30)
print "******".center(30)
print "****".center(30)
print "**".center(30)
print""
print""
print "A-3"
print "******"
print "*"
print "******"
print "*"
print "******"
print""
print""
print"±¸±¸´Ü"
print""
print""


x=2
while x<10:
    y=1
    while y<10:
        print x,"*",y,"=",x*y,x,"*",(y+1),"=",x*(y+1),x,"*",(y+2),"=",x*(y+2)
        y+=3
        print ''
    x+=1
    print ''
