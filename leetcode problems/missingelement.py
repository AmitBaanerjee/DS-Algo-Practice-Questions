#find the missing element from second list which is present in the first one

list1=[1,2,3,4,5,6,7,8]
list2=[8,1,2,4,7,3]
setinstance=set(list1)
for item in list2:
    if item in list1:
        setinstance.remove(item)
if len(setinstance)>0:
    for i in setinstance:
        print("element-->",i," missing from list2")
