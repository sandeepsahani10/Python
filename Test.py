list = ['sandeep', 10, 300.54]
print(list)
list.append('Hello')

print(list)
val = list[-1]
print(val)
list.append(7)

print(11 in list)

list[0]= 'rony'
print(list)

l1= list + ['Aundh', 'baner']
print(l1)

list.extend(['Pune','Mumbai'])

print(list)
del list[-1]
print(list.pop())

print (list)

l2 = [6,4,3,8,9,1,2,0]
l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)


a= ['Orange', 'Apple', 'Banana']
b=a
print(a,b)
a.append('jackfruit')
print(a,b)

p=['Orange', 'Apple', 'Banana']
q=p[:]
print(p,q)
p.remove('Orange')
print(p,q)

t=(1,2,3)
print(type(t))

names = ['Sandeep', 'Jipu', 'Saishree', 'Rony', 'Sandeep']
print(set(names))

nameTuple=('Sandeep', 'Sandeep','Sandeep')
print(type(nameTuple))
print('Printing the tuple as set>>', set(nameTuple))



list = ['sandeep', 10, 300.54]
print(list)
list.append('Hello')

print(list)
val = list[-1]
print(val)
list.append(7)

print(11 in list)

list[0]= 'rony'
print(list)

l1= list + ['Aundh', 'baner']
print(l1)

list.extend(['Pune','Mumbai'])

print(list)
del list[-1]
print(list.pop())

print (list)

l2 = [6,4,3,8,9,1,2,0]
l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)


a= ['Orange', 'Apple', 'Banana']
b=a
print(a,b)
a.append('jackfruit')
print(a,b)

p=['Orange', 'Apple', 'Banana']
q=p[:]
print(p,q)
p.remove('Orange')
print(p,q)

t=(1,2,3)
print(type(t))

names = ['Sandeep', 'Jipu', 'Saishree', 'Rony', 'Sandeep']
print(set(names))

nameTuple=('Sandeep', 'Sandeep','Sandeep')
print(type(nameTuple))
print('Printing the tuple as set>>', set(nameTuple))


# Set doesnt support indexing because it is not ordered

myset=set(nameTuple)
print(myset)
myset.add('Rony')

print(myset)

d1=[0,1,2,5,7,8,8]
d2=[9,4,5]
s1 = set(d1)
s2 = set(d2)

print('Union>>>',s1.union(s2))
print('Intersection>>', s1.intersection(s2))
print('Difference>>', s1.difference(s2))

dic1={100:'Sandeep', 101:'Rony'}
print(dic1[101])
dic1[103]='jipu'

print(dic1)
del dic1[100]
print(dic1)

dic1[100]='Sandeep'

print('Dict values::', dic1.values())
print('Dict keys::', dic1.keys())

dic1.update({100:'Sandy'})

print('Updated::>', sorted(dic1))

keys=sorted(dic1)
print('Keys is of type::',type(keys))
key=keys[0]
print('First employee is having id', key, ' with name ', dic1[key])

def check(x) :
    if(x > 10 or x ==10) :
        print('x is equal or greater than 10')
    else :
        print('x is not greater than 10')
        
        
check(10)

def login() :
    pin = input('Please enter your password')
    while(pin != '1234') :
        pin = input('Please enter a valid pin')
        
    print('You are logged in successfully')
    

login()


