class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        index2names = [None] * n
        index2emails = [[] for _ in range(n)]
        email2index = defaultdict(list)
        for i, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            index2names[i] = name
            index2emails[i] = emails
            for email in emails:
                email2index[email].append(i)

        # Traverse email2index for each person, find all the people use the same email
        visited_index = [False] * n
        ans = []  # names to emails
        for i in range(n):
            if visited_index[i]:
                continue
            # Find all emails for this person
            emails = set()
            people = deque([i])
            while people:
                person = people.popleft()
                visited_index[person] = True
                for email in index2emails[person]:
                    # get all people use the same email
                    for ppl in email2index[email]:
                        if not visited_index[ppl]:
                            people.append(ppl)
                    emails.add(email)
            
            instance = [index2names[i]] + sorted(list(emails))
            ans.append(instance)
        
        return ans


