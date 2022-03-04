# array are contiguous data structure
# we can traverse array 
'''
a = [10,1,23,4,5,6,7,7]
for ele in a:
    print(ele)
print("******")
a.append(1000)
print(a)

print("******")
a.pop()
print(a)
print("******")
a.remove(1)
print(a)
print("******")
a.sort()
print(a)
'''
# array rotation, rotate array elements by given count
# ex. a = [1,2,3,4,5,6] , rotate(a,2) should give a = [3,4,5,6,1,2]

def rotate(a,n):
    temp = []
    for i in range(n):
        temp.append(a[i])
    a = a[n:]
    print(a)
    print(temp)
    for ele in temp:
        a.append(ele)
    print(a)

a = [1,2,3,4,5,6]    
print(a)
print(rotate(a,2))