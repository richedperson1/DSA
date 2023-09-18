from collections import defaultdict

def accountsMerge( accounts):
    
    num = len(accounts)
    parent = [ind for ind in range(num)]
    dist = defaultdict(bool)
    for index in range(num):
        lastPoint = -1
        size = len(accounts[index])
        for ind in range(1,size):
            newEmail = accounts[index][ind]
            if newEmail not in dist:
                dist[newEmail] = index
            else:
                lastPoint = ind 
                break
        if lastPoint != -1:
            parent[index] = dist[accounts[index][lastPoint]]
            
            for ind in range(1,size):
                dist[accounts[index][ind]] = parent[index]

    
    mergeMail = defaultdict(list)
    for data,ind in dist.items():
        mergeMail[ind].append(data)


    newAccount = []
    for ind,data in mergeMail.items():
        firstIndex = accounts[ind][0]
        newData = data.append(firstIndex)
        newData = sorted(data)
        newAccount.append(newData)

    return newAccount

    return dist
accounts  =[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

print(accountsMerge(accounts))