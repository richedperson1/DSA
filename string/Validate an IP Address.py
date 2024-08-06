#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        size = len(strr)
        ind = 0
        
        total = 0
        flag = False
        while ind<size:
            if strr[ind]==".":
                return False
            
            local = ""
            while ind<size and strr[ind]!=".":
                local+= strr[ind]
                ind+=1
                flag = True
            
            if flag:
                flag = False
                total+=1
            
            if len(local)>1 and local[0]=="0":
                return False
                
            if int(local)<0 or int(local)>255:
                return False
                
            
            ind+=1
        if total!=4:
            return False
        return True
            
obj  = Solution()

string = "192.168.0.1"
print(obj.isValid(string))