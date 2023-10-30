def stringMatch(s,pattern):
    pattern  = pattern.split()
    distW2C = {}
    distC2W = {}
    if len(s)!=len(pattern):
        return False
    
    
    for char , word in zip(s,pattern):
        
        if distW2C.get(char,-1)==-1 and distC2W.get(word,-1)==-1:
            distW2C[char] = word
            distC2W[word] = char
            continue
        
        char2word = distW2C.get(char,-1)
        word2char = distC2W.get(word,-1)
        if distW2C.get(char,-1)!=word or distC2W.get(word,-1)!=char:
            return False
        
    return True

class Solution:
    def wordPattern(self, s: str, pattern) -> bool:
        pattern  = pattern.split()
        distW2C = {}
        distC2W = {}
        if len(s)!=len(pattern):
            return False


        for char , word in zip(s,pattern):

            if distW2C.get(char,-1)==-1 and distC2W.get(word,-1)==-1:
                distW2C[char] = word
                distC2W[word] = char
                continue

            if distW2C.get(char,-1)!=word or distC2W.get(word,-1)!=char:
                return False

        return True


s = "abba"
pattern = "dog cat cat dog"

obj = Solution()
print(obj.wordPattern(s,pattern))
print(stringMatch(s,pattern))