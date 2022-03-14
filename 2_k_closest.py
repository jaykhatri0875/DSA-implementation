# find k closest elements 
#give sorted integer array arr, two integers k and x, return k closest ints to x in array, result should be in sorted ascending order
# ex, |a-x| < |b-x| or 
# |a-x|==|b-x|  and a<b
    
arr = [1,2,3,4,5,6,7,8]
k = 3
x = 4
minar = []
for ele in arr:
    minar.append(abs(x-ele))

#print(minar)

def getEvenDigitNumbers(arr):
    leg = []
    for e in arr:
        if(len(str(e))%2==0):
            leg.append(e)
    return leg
print(getEvenDigitNumbers([42,5775,4,45,3556]))