class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            root_i = find(x)
            root_j = find(y)
            if root_i == root_j: return False
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_j] < rank[root_i]:
                parent[root_j] = root_i
            else: 
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        email_to_account = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        groups = defaultdict(set)
        for i, account in enumerate(accounts):
            root = find(i)
            for email in account[1:]:
                groups[root].add(email)
        result = []
        for root, emails in groups.items():
            emails_sort = sorted(emails)
            name_of_account = accounts[root][0]
            result.append([name_of_account] + emails_sort)
        return result
            