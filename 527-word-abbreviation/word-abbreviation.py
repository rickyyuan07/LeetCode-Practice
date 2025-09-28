class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n = len(words)
        prefixes = [1] * n
        abbrs = [self.make_abbr(word, 1) for word in words]
        
        while True:
            dup = defaultdict(list)  # abbr -> list[index]
            for i, abbr in enumerate(abbrs):
                dup[abbr].append(i)

            ok = True
            for abbr, dup_list in dup.items():
                if len(dup_list) <= 1:
                    continue
                ok = False
                for idx in dup_list:
                    prefixes[idx] += 1
                    new_abbr = self.make_abbr(words[idx], prefixes[idx])
                    abbrs[idx] = new_abbr
            
            if ok:
                break
        
        return abbrs

    def make_abbr(self, word, n_pre):
        n = len(word)
        if n - n_pre <= 2:
            return word
        return word[:n_pre] + str(n-n_pre-1) + word[-1]