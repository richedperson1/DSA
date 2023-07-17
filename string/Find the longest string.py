"""
! Link : https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-111/problems
"""


arr = list(map(str,"x gdwxo s brom rwfnhnvh gdm coicfjsswytzv ca co rwfnhnvvn gdwxynzqyk brop gdwxk gdwxynzqy coicfjsswc rwfk gd cox coicfjsswytk coicfjsswyt rwfnu coicfjsswytzybj rwfnhn rwfnhnvvi gdg ey rwfh coicfjsq coicfjss gdw rwfnha bj rwfnhnv coicfjsswy coicfm gdwxynzqj broe gd cw rwfnhno coz gdwxyd rv bror gf coicfjsswytzl gdwxynzqyrw rwfnhnvv coicfg gdwxynzqm efp rn coiq coic rwg gdwxyd i rwc coicfjsswytzybn ct o ef coicfjssa rwfnhnvp coicfjsswytzyj rwfn eu s j rwfnhnvl gl coick gdwc c coicf gdwxynzqyrg coicfjsswytz bro rwfnhnvvm gdwxynzi brp rwf coicfjsswye t b g by r coicfs coicfjsswytm gdwxy b rwk coicfj coicfjf coicfjsh coicd coicfjsswytzybb gdwxynzqyrz coicfjz gdwxynzq coicfjsswytzyb j coicfjsswytzyc coicfjs coicfjsz rwfnhnvvz rwfnhe rt coicfjssc coicfjsswyth coi rwfnc gdwxynzqyr coicfjssw gdwxynzqyb gdwxynzqyl coicfjsswytzyz brq gdwx p rwfnhna gdwxd brk coicfjsswyi gdg gdwxynz gdwxynx coicfjsswytzy rwfnhn ed gdwd coh efv j rwfo coicfjsswytzt coie gdwxynzqyrs br gdwh rwfnh coij t efw efd coicf gdwxynzz gdwxynr gdwxynzy gdwxynx b s coicfjsswa coicfjssz coicfjsswytzybl h rwfnhnb coicfjsswf gdwxyb gdwxynzqw coicfjsswyu gdwxyn coicfjs bh e rwfnf rw".split()))


from collections import Counter

def solution():
    def longestString( arr, n):
        #your code goes here
        def custom(str):
            return len(str)
        arr = sorted(arr,key=custom)
        
        dist = Counter(arr)
        ans = ""
        for data in reversed( arr):
            local = ""
            flag = True
            for char in data:
                local+=char
                if local not in dist:
                    flag = False
                    break
            if flag:
                # print(data)
                if len(ans)> len(data):
                    return ans
                
                if ans =="":
                    ans = data
                else:
                    ans = min(data,ans)
                
        
        return ans

    return longestString(arr,len(arr))


print(solution())