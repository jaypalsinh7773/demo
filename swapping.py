c=int(input("enter first number :"))
d=int(input("enter second number :"))

print("before swapping",c)
print("before swapping",d)

# temp=c
# c=d
# d=temp

# print("after swapping ",c)
# print("after swapping ",d)

# c,d=d,c

# print("after swapping ",c)
# print("after swapping ",d)

c=c+d
d=c-d
c=c-d

print("after swapping ",c)
print("after swapping ",d)