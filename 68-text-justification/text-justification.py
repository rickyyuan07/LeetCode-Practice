class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        ans = []
        curwords = []
        curwidth = 0
        for i in range(n-1):
            word = words[i]
            curwidth += (len(word) + 1)  # +1 for potential space
            curwords.append(word)
            if curwidth + len(words[i+1]) > maxWidth:
                # finish a line
                ret = self.justifyline(curwords, maxWidth)
                ans.append(ret)
                curwords = []
                curwidth = 0

        curwords.append(words[-1])
        curwidth += len(words[-1])
        lastline = ""
        for i in range(len(curwords)-1):
            lastline += curwords[i]
            lastline += " "
        lastline += curwords[-1]
        lastline += " " * (maxWidth - len(lastline))
        ans.append(lastline)
        
        return ans

    def justifyline(self, words, maxWidth):
        n = len(words)
        if n == 1:
            return words[0] + " "*(maxWidth - len(words[0]))
        total = sum(list(map(len, words)))
        spaces = maxWidth - total
        ret = ""
        for i, word in enumerate(words):
            ret += word
            # Deal with extra spaces if not devide evenly
            if spaces % (n-1) != 0:
                space = spaces // (n-1) + 1
                spaces -= 1
            else:
                space = spaces // (n-1)
            
            if i != n-1:
                ret += " " * space
        
        return ret
