#given number check whether or not is perfect square or not without using sqrt function


# this is binary search approach which checks in log(n) time complexity
def isSqrt(num):
    left,right = 1, num
    while left<=right:
        mid = (left+right)//2
        if mid*mid < num:
            left = mid+1
        elif mid*mid > num:
            right = mid-1
        else:
            return True
    return False

def isSqrtn(num):
    left,right = 1, num//2
    while(left<=right):
        mid = (left+right)//2
        if mid*mid == num:
            ans = mid
        elif mid*mid < num:
            left = mid+1
            ans = mid
        else:
            right = mid-1
    return ans	
	

print(isSqrtn(101))
#print(isSqrtn(16))
#print(isSqrtn(64))
#print(isSqrtn(120))
       