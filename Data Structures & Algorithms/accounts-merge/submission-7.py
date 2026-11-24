class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n+1))
        rank = [0]*(n+1)
        def find(x):
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j: return False
            if rank[root_j] < rank[root_i]: parent[root_j] = root_i
            elif rank[root_j] > rank[root_i]: parent[root_i] = root_j
            else: 
                parent[root_i] = root_j
                rank[root_j] += rank[root_i]
            return True
        email_to_account = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account: union(i, email_to_account[email])
                else: email_to_account[email] = i
        groups = defaultdict(set)
        for i, account in enumerate(accounts):
            root = find(i)
            for email in account[1:]:
                groups[root].add(email)
        result = []
        for root, emails in groups.items():
            email_sorted = sorted(emails)
            name_of_account = accounts[root][0]
            result.append([name_of_account] + email_sorted)
        return result

            