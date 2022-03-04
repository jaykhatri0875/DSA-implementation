#given number check whether or not is perfect square or not without using sqrt function


# this is binary search approach which checks in log(n) time complexity
def isSqrt(num):
    left,right = 1, num
    while left<=right:
        mid = (left+right)//2
        if mid*mid < num:
            left = mid+1
        elif mid*mid > num:
            right = mid-18
        else:
            return True
    return False

print(isSqrt(10))
print(isSqrt(16))
print(isSqrt(64))
print(isSqrt(120))
       