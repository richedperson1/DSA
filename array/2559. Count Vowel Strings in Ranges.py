from typing import List
def vowelStrings( words: List[str], queries: List[List[int]]) -> List[int]:
    
    sumi = [0]
    vowels = "aeiou"
    last = 0
    for data in words:
        if data[0] in vowels and data[-1] in vowels:
            last+=1
        sumi.append(last)
    
    results = []
    for query in queries:
        low = sumi[query[-1]+1]-sumi[query[0]]
        
        results.append(low)
    return results


words = ["baba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

print(vowelStrings(words,queries))