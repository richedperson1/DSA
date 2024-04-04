from collections import deque
from string import ascii_lowercase

class Solution:
    def wordLadderLength(self, startWord, tar, wordList):
        
        wordList = set(wordList)
        
        if startWord in wordList:
            wordList.remove(startWord)
            
        
        queue  = deque([(startWord,1)])
        
        while len(queue)>0:
            word,dist = queue.popleft()
            if word==tar:
                return dist
            
            for ind in range(len(word)):
                for char in ascii_lowercase:
                    newWord = word[:ind]+char+word[ind+1:]
                    if newWord in wordList:
                        queue.append((newWord,dist+1))
                        wordList.remove(newWord)
        return 0
    

arr   = ['des', 'der', 'dfr', 'dgt', 'dfs'] 
start = "der" 
end   = "dfs"
obj = Solution().wordLadderLength(start,end,arr)
print(obj)