# anshulmaurya27@gmail.com
l = []
r = 1
for i in range(0,10):
    r = r *13 %11
    if r == 1:
        r +=1
    x = str(r)
    l.append(x[0])

#print(l)
l=[*set(l)]
print(l,len(l))
    
