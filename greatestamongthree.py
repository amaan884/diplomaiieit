a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))
if a>b:
    if a>c:
        print("a is greatest",a)
    else:
        print("c is greatest",c)
elif b>c:
    print("b is greatest",b)
else:
    print("c is greatest",c)