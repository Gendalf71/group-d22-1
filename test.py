import mymod
print("Testing functions. Part-1")
print(mymod.mysum(1,2))
print(mymod.mysub(1,2))
print("Testing functions. Part-2")
print(mymod.mymul(1,2))
print(mymod.mydiv(1,2))
print("Finished testing")
c=mymod.mysum(1,2)+mymod.mysub(1,2)
d=mymod.mysum(1,2)-mymod.mysub(1,2)
e=mymod.mysum(1,2)*mymod.mysub(1,2)
f=mymod.mysum(1,2)*mymod.mysub(1,2)
print(c,d,e,f)
