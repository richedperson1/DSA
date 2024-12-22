#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        neg = -float("inf")
        
        ans = neg
        local = neg
        for data in arr:
            if data==0:
                ans = max(ans,local,data)
                neg = -float("inf")
                
            
            else:
                if data<0:
                    neg = max(data,neg)
                
                local *= data
        
        ans = max(local,ans)
       
