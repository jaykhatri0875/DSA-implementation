


def getPowerSet(nums):
    pow_size = pow(2,len(nums))
    counter = 0
    j = 0
    pset = []
    for counter in range(pow_size):
        for j in range(len(nums)):
            print((counter&(1<<j)))
            if((counter&(1<<j))>0):
                pset.append(nums[j])
        pset.append('x')
    return pset


items = [1,2,3,4]
print(getPowerSet(items))