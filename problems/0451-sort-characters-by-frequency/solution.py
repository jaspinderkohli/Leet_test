class Solution:
    def frequencySort(self, s: str) -> str:
        '''
            s = 'tree'
            dict {
                  t : 1
                  r : 1
                  e : 2
                } 
        '''
        dic = {}
        new_s = set(s)
        for char in new_s:
            dic[char] = s.count(char)

        sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

        ret = ''
        for k,v in sorted_dict.items():
            ret += k * v
        return ret
