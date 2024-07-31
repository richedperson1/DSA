
from typing import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        size = len(books)
        def dp_call(width,height,ind):
            if ind>=size:
                return 0 
            
            curr_book = books[ind]
            if curr_book[0]+width>shelfWidth:
                return dp_call(curr_book[0],curr_book[-1],ind+1)+curr_book[-1]
            
            else:
                if height>=curr_book[-1]:
                    first_call = dp_call(curr_book[0]+width,height,ind+1)
                    second_call = dp_call(curr_book[0],curr_book[-1],ind+1)+curr_book[-1]
                    return min(first_call,second_call)

                else: 
                    local_height = curr_book[-1]-height
                    first_call = dp_call(curr_book[0]+width,height+local_height,ind+1)+local_height
                    second_call = dp_call(curr_book[0],curr_book[-1] ,ind+1)+curr_book[-1]
                    return min(first_call,second_call)
        
        return dp_call(0,0,0)

obj = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4

books = [[1,3],[2,4],[3,2]]
shelfWidth = 6

books = [[1, 1000]] * 10  # 1000 books, each with thickness 1 and height 1000
print(books)
shelfWidth = 1

print(obj.minHeightShelves(books,shelfWidth))
            
            
            
        