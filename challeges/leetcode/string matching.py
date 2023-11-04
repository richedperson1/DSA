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

    """
    The `wordPattern` function checks if a given string `s` follows a given pattern by mapping each
    character in `s` to a word in `pattern` and vice versa.
    
    :param s: A string representing a sequence of characters
    :type s: str
    :param pattern: The `pattern` parameter is a string representing a pattern of characters. It is
    split into a list of words using the `split()` method
    :return: a boolean value.
    """

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