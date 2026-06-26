class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        uf = UnionFind(len(accounts))
        emailToAcc = {} #email -> index of acc

        for ac_idx, emails in enumerate(accounts):
            for email in emails[1:]:
                #The email is already in the emailToAcc hashmap
                #It means the email owner is same as the one inserted
                #Union two owner
                if email in emailToAcc:
                    uf.union(ac_idx, emailToAcc[email])
                else:
                    emailToAcc[email] = ac_idx

        emailGroup = defaultdict(list)# index of acc -> list of emails

        for email, ac_idx in emailToAcc.items():
            leader = uf.find(ac_idx)
            emailGroup[leader].append(email)

        res = []
        
        for leader_idx, emails in emailGroup.items():
            name = accounts[leader_idx][0]
            res.append([name] + sorted(emails))

        return res