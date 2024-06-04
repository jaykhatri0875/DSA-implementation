'
def majorityElement(self, A):
        candidate = None
        count = 0
        for element in A:
            if(candidate == element):
                count += 1
            elif(count == 0):
                candidate = element
            else:
                count -= 1
        count = 0
        for num in A:
            if(num == candidate):
                count += 1
        return candidate if count > len(A)//2 else None
