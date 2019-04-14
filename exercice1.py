numbers=[]
for i in range(2004,3200,7):
    if i%5!=0 : 
        numbers.append(i)
print (numbers)

factorial=1
x=input()
for i in range(1,int(x)+1):
    factorial=factorial*i
print (factorial)

dict1={}
x=input()
for i in range(1,int(x)+1):
    dict1[i]=i**2
print(dict1)

array2=[]
array1=input()
array1=array1.split(',')
for i in array1:
    array2.append(((2*50*int(i))/30)**0.5)
print (array2)