from collections import defaultdict
class FreqStack:

    def __init__(self):
        
        self.stack = defaultdict(list)
        self.freq  = defaultdict(int)
    def push(self, val: int) -> None:
        maxi = self.freq.get(val,0)+1
        self.stack[maxi].append(val)
        self.freq[val]+=1
        print("pushed : self.stack ==> ",self.stack)
        print("pushed : self.freq ==> ",self.freq)
        print("\n")
        

    def pop(self) -> int:
        # The line `result = max(self.stack)` is finding the key with the maximum frequency in the
        # `self.stack` dictionary. Since `self.stack` is a defaultdict with integer keys representing
        # frequencies and lists as values representing the elements with that frequency,
        # `max(self.stack)` will return the key with the highest frequency.
        # result = max(self.stack)
        while len(self.stack)>0:
            result = max(self.stack)
            if len(self.stack[result])>0:
                last_num = self.stack[result].pop()
                self.freq[last_num]-=1
                return last_num
            
            else:
                del self.stack[result]

        print("pop : self.stack ==> ",self.stack)
        print("pop : self.freq ==> ",self.freq)
        print("\n")
       
obj = FreqStack()


ops = ["push","push","push","push","push","push","pop","pop","pop","pop"]
val = [[5],[7],[5],[7],[4],[5],[],[],[],[]]



# Optimize Solution


from collections import defaultdict
class FreqStack:

    def __init__(self):
        
        self.stack = defaultdict(list)
        self.freq  = defaultdict(int)
        self.maxi = 0
    def push(self, val: int) -> None:
        maxi = self.freq.get(val,0)+1
        self.stack[maxi].append(val)
        self.freq[val]+=1
        self.maxi = max(maxi,self.maxi)
        

    def pop(self) -> int:
        # print("self.stack ==> ",self.stack)
        # print("self.stack ==> ",self.freq)
        try:
            result = self.stack[self.maxi].pop()
            self.freq[result]-=1
            if not (self.stack[self.maxi]):
                
                self.maxi -=1
            return result
        except:
            print("self.stack ==> ",self.stack)
            print("self.freq ==> ",self.freq)    
            print("self.maxi ==> ",self.maxi)    
            print("\n")
            
            
# ops = ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop","push","pop"]

# val = [[],[5],[7],[5],[7],[4],[5],[],[],[],[],[2],[]]
    
ops = ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]

val = [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]


optimize = FreqStack()
for ind in range(len(ops)):
    if ind==0:
        continue
    if ops[ind]=='push':
        optimize.push(val[ind][0])
    else:
        optimize.pop()
