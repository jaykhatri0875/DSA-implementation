from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
        n = len(A)
        dq = deque()
        ans = []
       
        for i in range(n):
            # Remove elements from the back of the deque as long as they are smaller than the current element
            while dq and A[i] >= A[dq[-1]]:
                dq.pop()
           
            # Add current element's index to the deque
            dq.append(i)
           
            # Remove elements that are outside the current window
            if dq[0] == i - B:
                dq.popleft()
           
            # If the window has reached its size, append the maximum element in the window to the result
            if i >= B - 1:
                ans.append(A[dq[0]])
       
        return ans
        """
        i,j=0,0
        k = B
		length = len(A)
        if(length == 1):
            return A
        if(B > length):
            return max(A)
        else:
            m = 0
            max_arr = []
            list_temp = []  
            while(j<length):
                
                #s = s + A[j]
                while(len(list_temp) and list_temp[-1] < A[j]):
                    list_temp.pop()
                list_temp.append(A[j])
                if(j-i+1 < k):
                    j += 1
                elif(j-i+1 == k):
                    max_arr.append(list_temp[0])
                    if(list_temp[0] == A[i]):
                        list_temp.pop(0) 
                    i += 1
                    j += 1
            return sum_arr
        """
