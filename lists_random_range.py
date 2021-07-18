import random
list1=[]
list2=[]

for i in range(1,101):
    v=random.randint(0,100)
    if (v%2)==0:
        list2.append(v)
    else:
        list1.append(v)

print('Odd_number_list= ', len(list1), 'Even_number_list= ',len(list2))
if sum(list2)-sum(list1)>0:
    print('Sum of elements of Even_list is more than Odd_list')
else:
    print('Sum of elements of Odd_list is more than Even_list')

#*******************************Dict

Dict_obj={'number of even elements=':len(list2), 'number of odd elements=': len(list1), 'sum of even elements =':sum(list2),'sum of odd elements=':sum(list1)}
print(Dict_obj)