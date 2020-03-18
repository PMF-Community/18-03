import math as m

xc = int(input('unesi x koordinatu centra: '))
yc = int(input('unesi y koordinatu centra: '))
r = int(input('unesi poluprecnik kruga: '))

xp = int(input('unesi x koordinatu tacke A: '))
yp = int(input('unesi y koordinatu tacke A: '))

d=m.sqrt(m.pow((xp-xc),2)-m.pow((yp-yc),2))

if d<r:
    print("tacka se nalazi u krugu")
elif d==r:
    print("tacka se nalazi na kruznici")
else:
    print("tacka je van kruznice")
