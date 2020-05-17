n=int(input("Enter the length of list"))
l=[]
final=[]
print("Enter the element")
for i in range(n+1):
    s=input()
    l.append(s)
for j in range(n+1):
    if l[j] not in final:
        final.append(l[j])
print(" list After removing duplicate:  ",final)

