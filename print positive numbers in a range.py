#Program to get input in form od list and print the positive values from the list

list=[]
s1=int(input("Size of list : "))
print("Enter elements in list[] : ")
for i in range (0,s1):
    n=int(input())
    list.append(n)
    i+=1
print("Positive elements are : ")
for i in list:
    if i>0:
        print(i)
