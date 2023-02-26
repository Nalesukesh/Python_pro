#print star
num=4

for i in range(num):
    for j in range(i):
        print("*",end="")
    print()
#print rev_str
s="sukesh nale"

def rev_str(s):
    new_str=""
    for i in s:
        new_str=i+new_str
    return new_str
print(rev_str(s))

#remove duplicate

dup=["sukesh","nale","sukesh"]
def remove_dup(dup):
    new_val=[]

    for i in dup:
        if i not in new_val:
            new_val.append(i)
    return new_val
print(remove_dup(dup))

#swap number
a=5
b=10

# a,b=b,a
# print(a)
# print(b)
temp=a
a=b
b=temp
print(a)
print(b)

#swap first and last value

number=[2,5,6,8,10]
count=len(number)

temp=number[0]
number[0]=number[count-1]
number[count-1]=temp

print(number)

#odd even number

L=[2,1,10,50,69,67,19,17]

for i in L:
    if i%2==0:
        print(i,"is even number")
    else:
        print(i,"is odd number")

#max min number

num2=[2,3,5,10,8,7,50,96,80,75,60]

max=num2[0]
size=len(num2)

for i in range(0,size):
    if num2[i]>max:
        max=num2[i]
print(max,"maximum number")

min=num2[0]

for i in range(0,size):
    if num2[i]<min:
        min=num2[i]
print(min,"minimum number")

#factorial
fact=0

num=5

for i in range(0,num+1):
     fact=fact+1
print(fact)





