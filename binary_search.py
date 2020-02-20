def binary_search(mylist,iskat,start,stop):
    if start>stop:
        return False
    else:
        mid = (start + stop)//2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binary_search(mylist,iskat,start,mid-1)
        else:
            return binary_search(mylist,iskat,start+1,stop)
mylist = [132,324,12,11,45,33,54]
mylist.sort()
print(mylist)
iskat = 132
start = 0
stop = len(mylist)

x = binary_search(mylist,iskat,start,stop)

if x == False:
    print('Элемент ',iskat,' не найден')
else:
    print('Элемент ',iskat, 'находится под индексом: ',x)
