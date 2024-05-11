class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        
        current_id,current_time = logs[0]
        
        maxi_tm = current_time
        maxi_id = current_id
        
        for emp_id,emp_time in logs:
            
            diff = emp_time-current_time
            if diff>=maxi_tm:
                if maxi_tm==diff:
                    maxi_id = min(maxi_id,emp_id)
                else:
                    maxi_id = emp_id
                    
                maxi_tm = diff
                
            current_id,current_time = emp_id,emp_time
        
        return maxi_id
    

obj = Solution()

# n    = 2
# logs = [[0,10],[1,20]]

n    = 10
logs = [[0,3],[2,5],[0,9],[1,15]]

print(obj.hardestWorker(n,logs))