n=int(input("enter a number"))
c=0
a=0
b=1
if n==0 or n==1:
    print("yes it belong to fibonacci seuence ")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("yes it belong to fibionacci sequnece ")
    else:
        print("no it does not belong to fibonacci sequence")
