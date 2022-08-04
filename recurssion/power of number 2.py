class Solution:
    # Complete this function
    modulo = 1000000007

    def power(self, n, r):
        if r == 0:
            return 1
        if r == 1:
            return n
        else:
            mid = r//2
            ans = self.power(n, mid)
            if r & 1:
                ans = (n % self.modulo*ans % self.modulo*ans %
                       self.modulo) % self.modulo
                return int(ans)
            else:

                return int((ans % self.modulo*ans % self.modulo) % self.modulo)
        # Your code here


n = 223
r = int(str(n)[::-1])
obj = Solution()
print(obj.power(n, r))
print(10e9+7)
