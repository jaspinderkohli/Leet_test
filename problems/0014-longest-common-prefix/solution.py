class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            iterate check - lowest 
        """
        if not strs:
            return ""
        min_len = float(inf)
        for x in strs:
            min_len = min(min_len, len(x))
        # if min_len
        for i in range(min_len):
            pref = (strs[0])[:i+1]
            for x in strs:
                if pref != x[:i+1]:
                    return (strs[0])[:i]
        
        return strs[0][:min_len]
