class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.par != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAcc = {}
        
        for i, emails in enumerate(accounts):
            for e in emails[1:]:
                if e not in emailToAcc:
                    emailToAcc[e] = i
                elif e in emailToAcc:
                    uf.union(i, emailToAcc[e])

        emailGroup = defaultdict(list) #root account to emails
        
        for e, i in emailToAcc.items():
            emailGroup[uf.find(i)].append(e)
        
        res = []

        for i, e in emailGroup.items():
            res.append([accounts[i][0]] + sorted(e))
        
        return res
        







