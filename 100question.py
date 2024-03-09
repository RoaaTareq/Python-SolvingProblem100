#create3elementson tuple
tuple=(1,2,3)
print(tuple)
# access second item omn list
list=[1,2,3]
print(list[1])
# add two num use function
def add_num(x ,y) :

    z=x+y
    print(z)
add_num(10,6)

# List VS Tuple
# List Ordered , Changable (Add , Remove,Update) , Dupliacte
# Tupler Ordered , unChangable (Add , Remove,Update) , Dupliacte  
#example List
list=[5,20,60]
list[1]=505
print(list) #changable
list=[50,20,30]
list.append(40)
print(list) #add

list=[50,20,30]
list.pop(2)
print(list) #Remove

list=[20,20,50,30]#duplicate
print(list)

#Tuple
tuple=(10,20,30,30)
print(tuple) # duplicate
 # remove (can't convert  to list  then back to tuple)
thistuple=(50,20,30)
newlist=list(thistuple)
newlist.append(40)
thistuple=tuple(newlist)
print(thistuple)

#find max number by 3 num
def maxNum(x, y, z):
    return max(x, y, z)

x = 200
y = 100
z = 20
max_num = maxNum(x, y, z)
print("The maximum number is:", max_num)

# check key on dic
thisdic={
    "brand":"Ford",
    "model":"BMW",
    "year":1950
}

if "model" in thisdic:
    print('yes')


#creat set with  element
setlist=(20,30,40)
print(setlist)

#print number 1 to 5 use loop
for x in range(1,6) :
   print(x)

#convert list to set 
   
thislist=[1,2,3]
thisset=set(list)
print(thisset)
