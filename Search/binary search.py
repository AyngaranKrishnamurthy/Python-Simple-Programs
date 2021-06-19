l=[]
n1=int(input("Enter the number of elements in the list"))
i=0
while(i<n1):
    a=int(input("Enter the value"))
    l.insert(i,a)
    i=i+1
l.sort()
n=int(input("\n enter the value to be found\n"))
first=0
last=n1-1
middle=(first+last)//2
while(first<=last):
    if(l[middle]<n):
        first=middle+1
    elif(l[middle]==n):
        print(n,"found at location",middle+1)
        break
    else:
        last=middle-1
        middle=(first+last)//2
if(first>last):
    print(n,"is not found in the list")