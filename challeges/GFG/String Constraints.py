MAX_CHAR = 9

def check(freq, k):
    for i in range(0, MAX_CHAR):
        if(freq[i] and freq[i] != k):
            return False
    return True

def substrings(s, k):
    res = 0 
    for i in range(0, len(s)):

        freq = [0] * MAX_CHAR
 
        for j in range(i, len(s)):
             
            index = int(s[j])
            freq[index] += 1

            if(freq[index] > k):
                break
             

            elif(freq[index] == k and
                 check(freq, k) == True):
                res += 1
             
    return res


def CountStrings( s : str) -> int:
    # code here
    maxi = 0
    for data in s:
        maxi = max(maxi,int(data))
        
    size = len(s)
    count = 0
    for ind in range(size):
        freq = {}
        local = ""
        for i in range(ind,size):
            local+=s[i]
            letterFreq = freq.get(s[i],0)+1
            if letterFreq>=maxi:
                break
            freq[s[i]] = letterFreq
            count+=1
            print(local)
            
    return count

s = "122321"
k = 3
print(CountStrings(s))

