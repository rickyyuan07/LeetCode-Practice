class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_length = len(target)
        n_state_space = 1 << target_length
        # Construct the stickers number of characters:
        stickers_dict = []
        for i, sticker in enumerate(stickers):
            stickers_dict.append(Counter(sticker))
        
        # print(stickers_dict)
        stickers_l = [[0] * 26 for _ in range(len(stickers))]
        for ii, dd in enumerate(stickers_dict):
            for i in range(26):
                ch = chr(i+ord('a'))
                if ch in stickers_dict[ii]:
                    stickers_l[ii][i] = stickers_dict[ii][ch]

        # Preprocess: n, s -> s'; Applied sticker i from state s to which s'?
        state_trans = [[0] * n_state_space for _ in range(len(stickers))]
        for i in range(len(stickers)):
            for s in range(n_state_space):
                sticker = stickers_l[i].copy()
                new_s = s
                for b in range(target_length):
                    if not (s >> b) & 1:
                        c = target[b]
                        if sticker[ord(c)-ord('a')] > 0:
                            sticker[ord(c)-ord('a')] -= 1
                            new_s |= (1 << b)

                state_trans[i][s] = new_s
        
        # if it's possible to use i stickers to form state
        dp = [float("inf")] * n_state_space
        dp[0] = 0
        for s in range(n_state_space):
            if dp[s] == float("inf"):
                continue
            for i in range(len(stickers)):
                ns = state_trans[i][s]
                dp[ns] = min(dp[ns], dp[s] + 1)

        return -1 if dp[n_state_space - 1] == float("inf") else dp[n_state_space - 1]

