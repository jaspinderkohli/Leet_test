class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        all_chr = []
        for i, x in enumerate(words):
            for y in x:
                if y not in all_chr:
                    all_chr.append(y)
        # print all_chr
        cmn = []
        for x in all_chr:
            nl = []
            for y in words:
                n = y.count(x)
                nl.append(n)
            cnt = min(nl)
            if cnt:
                print x, cnt
                cmn += [x]*cnt
                
        return cmn
